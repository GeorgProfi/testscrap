import scrapy


class TagsSpider(scrapy.Spider):
    name = "tags"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def start_requests(self):
        yield scrapy.Request(
            url = f'https://quotes.toscrape.com',
            callback=self.parse
        )


    def parse(self, response):
        toptag = response.xpath('//span[@class="tag-item"]/a/text()').getall()
        for i in range(len(toptag)):
            yield {f'{i}' : toptag[i]}


