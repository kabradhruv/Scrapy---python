import scrapy
from ..items import HomeItem

# Use these commands in the terminal to get the result as an output
'''
scrapy crawl IndianExpress -o res.json
scrapy crawl IndianExpress -o res.csv
scrapy crawl IndianExpress -o res.xml
'''

# items.py file code - 
'''
import scrapy
class HomeItem(scrapy.Item):
    # Indian Express 
    topNews = scrapy.Field()
'''

class TimesOfIndia(scrapy.Spider):

    # extracting top news from indian express
    name = "IndianExpress"
    start_urls = ["https://timesofindia.indiatimes.com/"]
    def parse(self, response):
        items = HomeItem()
        figCaption=response.css('.Q6d5H figcaption::text').extract()
        items['topNews'] = figCaption
        yield items



    
