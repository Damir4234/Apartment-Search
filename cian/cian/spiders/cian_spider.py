import scrapy


class CianSpiderSpider(scrapy.Spider):
    name = "cian_spider"
    allowed_domains = ["kazan.cian.ru"]
    start_urls = ["https://kazan.cian.ru"]

    def parse(self, response):
        pass
