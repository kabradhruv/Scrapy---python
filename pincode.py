import scrapy
from ..items import HomeItem

# Use these commands in the terminal to get the result as an output
'''
scrapy crawl pincode -o res.json
scrapy crawl pincode -o res.csv
scrapy crawl pincode -o res.xml
'''

# items.py file code - 
'''
import scrapy
class HomeItem(scrapy.Item):
    #pincode
    name = scrapy.Field()
    address = scrapy.Field()
'''

class TimesOfIndia(scrapy.Spider):

    #Pagination next page button pincode

    name = "pincode"
    start_urls = ["https://pin-code.org.in/companies/sector/agriculture"]

    def parse(self, response):
        items = HomeItem()
        # boxDetails=response.css('div.boxDetails')
        # name = boxDetails.css('h5 a::text').extract()
        # address = boxDetails.css('p::text').extract()

        name = response.css('#company a::text').extract()
        address = response.css('.address::text').extract()

        items['name'] = name
        items['address'] = address

        yield items

        nextPage = response.css('li.page-link')[-1].css('a::attr(href)').get()
        if nextPage is not None:
            print("Next page link is " + nextPage)
            yield response.follow(nextPage , callback = self.parse)
    
    
