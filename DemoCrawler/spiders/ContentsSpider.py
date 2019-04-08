import scrapy

class ContentsSpider(scrapy.Spider):
    name = "contents"

    def start_requests(self):
        urls = [
            'https://blogradio.vn/yeu-247/chenh-venh-mua-hoa-sua/217153'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//h1[@class="title"]/text()').get()
        author = response.xpath('//p[@class="auth"]/span/a/text()').get()
        filename = 'contents.txt'
        with open(filename, 'w') as f:
            f.write(title + '\n')
            f.write(author)
        self.log('Saved file %s' % filename)