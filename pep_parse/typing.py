from scrapy import Item, http, Spider


ItemType = Item | dict
ResponseType = http.Response
SpiderType = Spider

# На ЯП не проходит тесты так как там Python 3.7
# from typing import TypeAlias
# ItemType: TypeAlias = PepParseItem
# ResponseType: TypeAlias = Response
