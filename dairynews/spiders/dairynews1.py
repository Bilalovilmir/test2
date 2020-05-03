# -*- coding: utf-8 -*-
import scrapy


class Dairynews1Spider(scrapy.Spider):
    name = 'dairynews1'
    allowed_domains = ['https://www.dairynews.ru/company/']
    start_urls = ['http://https://www.dairynews.ru/company/']

    def parse(self, response):
        pass
