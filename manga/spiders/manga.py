import scrapy
from ..items import MangaItem


class my_first_scrapy(scrapy.Spider):
    name = 'manga'
    start_urls = [
        'https://mangarock.herokuapp.com/'
    ]

    def parse(self, response):

        slider_items = MangaItem()


        slider_items['img_src'] = response.xpath('//div[@class="item"]/img/@src').getall()
        slider_items['title'] = response.xpath('//div[@class="slide-caption"]/h3/a/text()').getall()
        slider_items['chapter_id'] = response.xpath('//div[@class="slide-caption"]/a/text()').getall()


        yield slider_items
