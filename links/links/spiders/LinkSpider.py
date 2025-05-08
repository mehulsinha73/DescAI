from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from links.links.items import UrlItem
from urllib.parse import urlparse

class LinkSpider(CrawlSpider):
    name = 'links'

    rules = (
        Rule(LinkExtractor(), callback='parse_url'),
    )

    def __init__(self, **kw):
        super(LinkSpider, self).__init__(**kw)
        self.allowed_domains = kw.get("allowed_domains")
        self.start_urls = kw.get("start_urls")
        self.custom_settings = kw.get("custom_settings")

    def parse_url(self, response):
        item = UrlItem()
        item['url'] = response.url
        item['domain'] = urlparse(response.url).netloc
        return item
