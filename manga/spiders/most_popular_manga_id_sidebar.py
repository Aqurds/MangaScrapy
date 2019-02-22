import scrapy
import json
from ..items import PopularMangaList




# This spider will collect all the popular manga ID from front-page
class my_first_scrapy(scrapy.Spider):
    name = 'popular_manga_list'

    start_urls = [
            'https://mangarock.herokuapp.com/'
    ]


    def parse(self, response):

        popular_manga_list = PopularMangaList()


        manga_full_url = response.xpath('//div[@class="slide-caption"]/h3/a/@href').extract()
        popular_manga = []
        for id in manga_full_url:
            popular_manga.append(id.split('/')[-1])
        popular_manga_list['popular_manga_id'] = popular_manga

        yield popular_manga_list

# Create popular_manga_list.json file
