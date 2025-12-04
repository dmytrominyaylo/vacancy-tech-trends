import scrapy
from jobs_scraper.items import JobsScraperItem
from w3lib.html import remove_tags
import re


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["work.ua"]
    start_urls = [f"https://www.work.ua/jobs-python/?page={i}" for i in range(1, 6)]

    custom_settings = {
        "FEEDS": {
            "jobs.jl": {
                "format": "jsonlines",
                "encoding": "utf8",
                "overwrite": True,
            }
        }
    }

    def clean(self, text):
        """Очищення тексту від HTML та зайвих пробілів"""
        if not text:
            return None
        txt = remove_tags(text)
        txt = re.sub(r"\s+", " ", txt)
        return txt.strip()

    def parse(self, response):
        """Парсинг сторінки списку вакансій"""
        job_blocks = response.css("div.job-link, div.card.card-hover.card-visited")
        self.logger.info("Found %d job blocks on page %s", len(job_blocks), response.url)

        for job in job_blocks:
            link = job.css("a::attr(href)").get()
            if link:
                yield response.follow(response.urljoin(link), callback=self.parse_job)

    def parse_job(self, response):
        """Парсинг однієї вакансії для JobsScraperItem"""

        item = JobsScraperItem()

        # TITLE
        title = response.css("h1::text").get() or response.xpath("//h1/text()").get()
        item["title"] = title.strip() if title else None

        # COMPANY
        company = (
            response.xpath('//a[contains(@href,"/companies")]/text()').get()
            or response.xpath('//p[contains(@class,"company")]/a/text()').get()
            or response.xpath('//div[contains(@class,"company")]//text()').get()
        )
        item["company"] = company.strip() if company else None

        # LOCATION
        location = (
            response.css(".place::text").get()
            or response.xpath('//li[contains(@class,"location")]/text()').get()
            or response.xpath('//p[contains(@class,"location")]/text()').get()
            or response.xpath('//span[contains(text(),"м.")]/text()').get()
        )
        item["location"] = location.strip() if location else None

        # EXPERIENCE
        experience = (
            response.xpath('//div[contains(text(),"Досвід")]/following-sibling::div/text()').get()
            or response.xpath('//p[contains(.,"Досвід")]/text()').get()
        )
        item["experience"] = self.clean(experience) if experience else None

        # SALARY
        salary = (
            response.xpath('//div[contains(@class,"salary")]//text()').get()
            or response.xpath('//b[contains(@class,"salary")]/text()').get()
            or response.xpath('//p[contains(.,"грн") or contains(.,"$")]/text()').re_first(r'[\d\s\$–-]+')
        )
        item["salary"] = salary.strip() if salary else None

        # LINK
        item["link"] = response.url

        # DESCRIPTION
        desc_parts = (
            response.xpath('//div[contains(@class,"job-description")]//text()').getall()
            or response.xpath('//article//text()').getall()
            or response.xpath('//div[contains(@class,"content")]//text()').getall()
        )
        description = " ".join(p.strip() for p in desc_parts if p and p.strip()) if desc_parts else None
        item["description"] = re.sub(r"\s+", " ", description).strip() if description else None

        # DATE POSTED
        date_posted = (
            response.xpath('//span[contains(@class,"text-muted")]/text()').re_first(r'\d{1,2}\s+\w+')
            or response.xpath('//p[contains(@class,"text-muted")]/text()').re_first(r'\d{1,2}\s+\w+')
        )
        item["date_posted"] = date_posted.strip() if date_posted else None

        yield item
