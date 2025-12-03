import scrapy
from dou_scraper.items import DouScraperItem


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["dou.ua"]
    start_urls = ["https://dou.ua/jobs/?category=Python"]

    custom_settings = {
        "FEEDS": {
            "jobs.jl": {
                "format": "jsonlines",
                "encoding": "utf8",
                "overwrite": True,
            }
        }
    }

    def parse(self, response):
        for job_link in response.css("div.vacancy a.vacancy-title::attr(href)").getall():
            yield response.follow(job_link, callback=self.parse_job)

        next_page = response.css("a.pagination-next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_job(self, response):
        item = DouScraperItem()
        item["title"] = response.css("h1.h1::text").get(default="").strip()
        item["company"] = response.css("div.terms a::text").get(default="").strip()
        item["location"] = response.css("div.place::text").get(default="").strip()
        item["experience"] = response.css("div.terms span.experience::text").get(default="").strip()
        item["salary"] = response.css("div.salary span::text").get(default="").strip()
        item["link"] = response.url
        item["description"] = response.css("div.vacancy-description").get(default="").strip()
        item["date_posted"] = response.css("time::attr(datetime)").get(default="").strip()
        yield item
