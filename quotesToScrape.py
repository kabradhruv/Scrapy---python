import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import HomeItem

# Use these commands in the terminal to get the result as an output
'''
scrapy crawl quotes -o res.json
scrapy crawl quotes -o res.csv
scrapy crawl quotes -o res.xml
'''

# items.py file code - 
'''
import scrapy
class HomeItem(scrapy.Item):
    # Quotes to Scrape 
    quote = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
'''

class TimesOfIndia(scrapy.Spider):

    # extracting top news from Quotes to scrape

    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/login"]

    def parse(self, response):
        token=response.css('form input::attr(value)').extract_first()

        # this return function i.e. from_response() take 3 parameter
        """
        1. response
        2. form data = {csrf_token,username,password}          //according to this website
        3. callback         // where to go now
        """
        
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'abcdef',
            'password' : 'abcdef'
        } , callback = self.start_scraping)
        
    def start_scraping(self,response):
        items = HomeItem()
        # open_in_browser(response)

        quote = response.css(".text::text").extract()
        author = response.css(".author::text").extract()
        tag = response.css(".tag::text").extract()

        items['quote'] = quote
        items['author'] = author
        items['tag'] = tag

        yield items



    
