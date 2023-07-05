import scrapy

class TestSpider (scrapy.Spider):
    name = "firstSpider"
    stat_urls = ["https://quotes.toscrape.com"]

    def parse (self, response):

        for card in response.css("div.quote"):
            tags = card.css("div.tags a.tag::text").getall()
            yield { 'text' : card.css("span.text::text").get() }
