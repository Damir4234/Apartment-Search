import scrapy


class CianSpiderSpider(scrapy.Spider):
    name = "cian_spider"
    allowed_domains = ["kazan.cian.ru"]
    start_urls = ["https://kazan.cian.ru/sale/flat/301723007/"]

    def parse(self, response):
        title = response.css('.a10a3f92e9--title--vlZwT::text').get()
        space = response.css('.a10a3f92e9--color_black_100--Ephi7 a10a3f92e9--lineHeight_6u--cedXD a10a3f92e9--fontWeight_normal--JEG_c a10a3f92e9--fontSize_16px--QNYmt a10a3f92e9--display_block--KYb25 a10a3f92e9--text--e4SBY a10a3f92e9--text_letterSpacing__0--cQxU5::text').get()
        floor = response.xpath(
            '//*[@id="frontend-offer-card"]/div/div[2]/div[2]/div[4]/div[2]/div[2]/span[2]/text()').get()
        address = response.xpath(
            '//*[@id="frontend-offer-card"]/div/div[2]/div[2]/section/div/div/div[2]/address/div/div/a[4]/text()').get()
        price = None

        print(f"{title}, {space}, {floor}, {address}")
