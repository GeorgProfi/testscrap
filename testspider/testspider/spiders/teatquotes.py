import scrapy
from pathlib import Path

class TeatquotesSpider(scrapy.Spider):
    name = "teatquotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def start_requests(self):
        start_page = 1
        urls = []
        for page in range(10): # на сайте 10 стр, по хорошему придумать метод нахождения количества стр
            yield scrapy.Request(f"https://quotes.toscrape.com/page/{start_page}/", callback=self.parse)
            start_page += 1



    def parse(self, response):
        for card in response.css("div.quote"):  # div[@class="quote"]
            tags = card.css("div.tags a.tag::text").getall()
            yield {
                'text': card.css("span.text::text").get(),
                'author': card.css("small.author::text").get(),
                'tags': tags
            }
