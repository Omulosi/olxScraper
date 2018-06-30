import scrapy
from olxScraper.items import OlxscraperItem

class OlxSpider(scrapy.Spider):
    name = 'vehicles'
