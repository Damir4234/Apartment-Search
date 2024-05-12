import scrapy


class CianSpiderSpider(scrapy.Spider):
    name = "cian_spider"
    allowed_domains = ["kazan.cian.ru"]
    start_urls = ["https://kazan.cian.ru/sale/flat/301723007/"]

    def parse(self, response):
        title = response.css('.a10a3f92e9--title--vlZwT::text').get()
        print(title)
