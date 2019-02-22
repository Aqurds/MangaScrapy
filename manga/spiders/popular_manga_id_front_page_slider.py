import scrapy
import json
from ..items import MostPopularMangaList




# This spider will collect most popular manga id from front-page sidebar
class my_first_scrapy(scrapy.Spider):
    name = 'most_popular_manga_list_sidebar'

    start_urls = [
            'https://mangarock.herokuapp.com/'
    ]


    def parse(self, response):

        most_popular_manga_list = MostPopularMangaList()


        manga_full_url = response.xpath('//div[@class="xem-nhieu-item"]/h3/a/@href').extract()
        most_popular_manga = []
        for id in manga_full_url:
            most_popular_manga.append(id.split('/')[-1])
        most_popular_manga_list['most_popular_manga_id_sidebar'] = most_popular_manga

        yield most_popular_manga_list

# Create most_popular_manga_list_sidebar.json file
