from scrapy import Spider

from pep_parse.items import PepParseItem
from pep_parse.typing import ItemType, ResponseType


class PepSpider(Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: ResponseType) -> ItemType:
        yield from response.follow_all(
            response.css('#numerical-index tbody a'),
            callback=self.parse_pep
        )

    def parse_pep(self, response: ResponseType) -> ItemType:
        number, name = response.css('.page-title::text').get().split(' – ')
        yield PepParseItem({
            'number': int(number.split()[1]),
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        })
