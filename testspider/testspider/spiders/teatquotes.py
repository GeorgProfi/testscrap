import scrapy
from pathlib import Path

class TeatquotesSpider(scrapy.Spider):
    name = "teatquotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def start_requests(self):
        url = "https://quotes.toscrape.com"
        yield scrapy.Request(url, callback= self.parse)

    def parse(self, response):
        for card in response.css("div.quote"):  # div[@class="quote"]
            tags = card.css("div.tags a.tag::text").getall()
            yield {
                'text': card.css("span.text::text").get(),
                'author': card.css("small.author::text").get(),
                'tags': tags
            }
