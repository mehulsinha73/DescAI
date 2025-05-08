# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field


class UrlItem(Item):
    url = Field()
    domain = Field()
