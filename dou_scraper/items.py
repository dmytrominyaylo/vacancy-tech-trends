# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouScraperItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    experience = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    date_posted = scrapy.Field()
