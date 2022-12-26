import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        yield from response.follow_all(
            response.css(
                'section[id^="numerical-index"]').css('tbody a'),
            callback=self.parse_pep
        )

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split(' – ')
        number = int(number.split()[1])
        yield PepParseItem({
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd').css('abbr::text').get(),
        })
