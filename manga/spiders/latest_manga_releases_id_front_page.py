import scrapy
import json
from ..items import LatestMangaReleasesIdFrontPage




# This spider will collect all the popular manga ID from front-page
class my_first_scrapy(scrapy.Spider):
    name = 'Latest_manga_releases_id_front_page'

    start_urls = [
            'https://mangarock.herokuapp.com/'
    ]


    def parse(self, response):

        latest_releases_manga_list = LatestMangaReleasesIdFrontPage()


        manga_full_url = response.xpath('//a[@class="tooltip"]/@href').extract()
        latest_releases_manga = []
        for id in manga_full_url:
            latest_releases_manga.append(id.split('/')[-1])
        latest_releases_manga_list['Latest_manga_releases_id_front_page'] = latest_releases_manga

        yield latest_releases_manga_list

# Create Latest_manga_releases_id_front_page.json file
