# python 3
from dairynews.items import DairynewsItem
import scrapy
from urllib.parse import urljoin
  
class DairynewsSpider(scrapy.Spider):
	name = 'dairynews'
	allowed_domains = ['dairynews.ru']
	start_urls = ['https://www.dairynews.ru/company/']
	custom_settings={ 'FEED_URI': "dairynews_%(time)s.csv",
					'FEED_FORMAT': 'csv'}

	def parse(self, response):
		for link in response.xpath("//a[@class='table-name-link']/@href").extract():
				url = urljoin(response.url, link.replace("/company/",""))
				yield response.follow(url, callback=self.parse_company)

	def parse_company(self, response):
		item = DairynewsItem()
		title=response.xpath("//div[@class='company-head__name']/text()").extract()
		item['name']=title

		holding=response.xpath("//div[@class='company-head__name']/a[@class='holding-company']/div[@class='btn-text']/text()").extract()
		item['holding']=holding

		address=response.xpath("//div[@class='contact-block__text contact-block__text--address']/text()").extract()
		item['address']=address

		tel_email=response.xpath("//div[@class='company-contacts__item']//div[@class='contact-block__text']/text()").extract()
		item['tel_email']=tel_email

		yield item