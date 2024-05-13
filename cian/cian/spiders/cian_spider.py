import scrapy


class CianSpiderSpider(scrapy.Spider):
    name = "cian_spider"
    allowed_domains = ["kazan.cian.ru"]
    start_urls = [
        "https://kazan.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=4777&room1=1"]

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json'
    }

    def parse(self, response):

        flat_urls = response.css(
            'a._93444fe79c--link--eoxce::attr(href)').getall()
        for url in flat_urls:
            yield scrapy.Request(url, callback=self.parse_flat)

    def parse_flat(self, response):

        title = response.css('.a10a3f92e9--title--vlZwT::text').get()
        space = response.css(
            '.a10a3f92e9--item--Jp5Qv:nth-child(1) .a10a3f92e9--fontSize_16px--QNYmt::text').get()
        floor = response.xpath(
            '//*[@id="frontend-offer-card"]/div/div[2]/div[2]/div[3]/div[4]/div[2]/span[2]/text()').get()
        address = response.xpath(
            '//*[@id="frontend-offer-card"]/div/div[2]/div[2]/section/div/div/div[2]/address/div/div/a[4]/text()').get()
        price = response.xpath(
            '//div[@data-testid="price-amount"]/span/text()').get()
        id_url = response.url.split('/')[-2]

        floor_elements = response.css('.a10a3f92e9--item--Jp5Qv')
        floor = None
        for element in floor_elements:
            label = element.css('.a10a3f92e9--text--eplgM span::text').get()
            if label == 'Этаж':
                floor = element.css(
                    '.a10a3f92e9--text--eplgM span:nth-child(2)::text').get()
                break

        yield {
            'title': title,
            'space': space,
            'floor': floor,
            'address': address,
            'price': price,
            'id_url': id_url
        }
