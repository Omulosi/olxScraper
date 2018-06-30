import scrapy
from olxScraper.items import OlxscraperItem

class OlxSpider(scrapy.Spider):
    name = 'vehicles'
    allowed_domains = ['www.olx.com.pk']

    start_urls = ['https://www.olx.com.pk/vehicles/']

    def parse(self, response):
        i = 0
        for v in response.css('li.lpv-item'):
            desc = v.css('.lpv-item-info--description h3::text').extract_first().strip()
            price = v.css('.lpv-item-info--price::text').extract_first().strip()
            url = v.css('.lpv-item-link::attr(href)').extract_first()
            print('Desc: '+desc)
            print('price: '+price)
            print('Link: '+url)
            print(i)
            i += 1
            item = OlxscraperItem()
            item['description'] = desc
            item['price'] = price
            item['link'] = url
            yield item
        
        """
        next_page = response.css('.lpv-item-link::attr(href)').extract_first()
        if next_item is not None:
            yield response.follow(next_page, callback=self.parse)

        """


