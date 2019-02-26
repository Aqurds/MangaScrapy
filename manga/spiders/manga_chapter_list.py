import scrapy
import json
from ..items import MangaChapterList




# This spider will use the individual manga url from the json file and will crawl each individual manga page and will collect all the chapter details
class my_first_scrapy(scrapy.Spider):
    name = 'manga_chapter_list'

    start_urls = []
    url_dict = ''

    with open('manga_name.json', 'r') as f:
        url_dict = json.load(f)

    for item in url_dict:
        for key, val in item.items():
            for url in val:
                start_urls.append(url)

    def parse(self, response):

        manga_chapter_list = MangaChapterList()



        manga_chapter_list['manga_id'] = response.xpath('//div[@class="row"]/span[1]/a/@href')[0].extract().split('/')[-2]

        chapter_full_url = response.xpath('//div[@class="row"]/span[1]/a/@href').extract()
        chapter_id_list = []
        for id in chapter_full_url:
            chapter_id_list.append(id.split('/')[-1])
        manga_chapter_list['chapter_id'] = chapter_id_list

        manga_chapter_list['full_chapter_url'] = response.xpath('//div[@class="row"]/span[1]/a/@href').extract()
        manga_chapter_list['chapter_link_text'] = response.xpath('//div[@class="row"]/span[1]/a/text()').extract()
        # manga_chapter_list['chapter_view'] = response.xpath('//div[@class="row"]/span[2]/text()').extract()
        manga_chapter_list['chapter_time_uploaded'] = response.xpath('//div[@class="row"]/span[3]/text()').extract()



        yield manga_chapter_list

# Create manga_chapter_list.json file
