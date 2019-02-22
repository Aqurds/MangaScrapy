import scrapy
import json
from ..items import RelatedMangaSuggestionInChapterView




# This spider will collect all of manga ID from chapter view page
class my_first_scrapy(scrapy.Spider):
    name = 'related_manga_suggestion_in_chapter_view'

    start_urls = [
            'https://mangarock.herokuapp.com/chapter/usogui/chapter_1'
    ]


    def parse(self, response):

        related_manga_suggestion_in_chapter_view = RelatedMangaSuggestionInChapterView()


        manga_full_url = response.xpath('//h3[@class="nowrap"]/a/@href').extract()
        manga_id_list = []
        for id in manga_full_url:
            manga_id_list.append(id.split('/')[-1])
        related_manga_suggestion_in_chapter_view['related_manga_suggestion_in_chapter_view'] = manga_id_list

        yield related_manga_suggestion_in_chapter_view

# Create related_manga_suggestion_in_chapter_view.json file
