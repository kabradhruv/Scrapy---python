import scrapy
from ..items import AmazonItem


class AmazonscrapeSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.in/s?k=mobile&crid=3PVZ8HKT5TGC7&sprefix=mobile%2Caps%2C254&ref=nb_sb_noss_1"]
    page_number = 2

    def parse(self, response):
        items = AmazonItem()
        title = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('#search .a-price-whole::text').extract()
        img = response.css('.s-image::attr(src)').extract()
        items['title'] = title
        items['price'] = price
        items['img'] = img
        yield items

        next_page="https://www.amazon.in/s?k=mobile&page="+str(AmazonscrapeSpider.page_number)+"&crid=3PVZ8HKT5TGC7&qid=1682184689&sprefix=mobile%2Caps%2C254&ref=sr_pg_1"

        if AmazonscrapeSpider.page_number <= 100:
            AmazonscrapeSpider.page_number+=1
            yield response.follow(next_page,callback = self.parse)

