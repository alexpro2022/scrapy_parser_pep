import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        yield from response.follow_all(
            response.css('#numerical-index tbody a'),
            callback=self.parse_pep
        )

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split(' – ')
        yield PepParseItem({
            'number': int(number.split()[1]),
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        })
