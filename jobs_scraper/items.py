import scrapy


class JobsScraperItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    experience = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    date_posted = scrapy.Field()
