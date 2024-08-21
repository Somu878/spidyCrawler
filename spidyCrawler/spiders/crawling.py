from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class crawlingspidy(CrawlSpider):
    name = "spidy"
    allowed_domains = ["toscrape.com"]
    #add a proxy server to avoid rate-limit ban
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category"), follow=True),
        Rule(LinkExtractor(allow='catalogue',deny='category'),callback="parse_item")
    )

    def parse_item(self, response):
        yield{
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
             "availability": response.css(".availability::text")[1].get().strip()
        }
