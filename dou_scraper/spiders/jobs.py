import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["dou.ua"]
    start_urls = ["https://dou.ua"]

    def parse(self, response):
        pass
