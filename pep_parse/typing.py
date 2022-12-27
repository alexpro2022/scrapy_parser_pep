from typing import Iterable

from scrapy import crawler, Item, http, Spider


CrawlerType = crawler.Crawler
ExceptionType = Exception
ItemType = Item
RequestType = http.Request
ResponseType = http.Response
ResultType = Iterable[ItemType]
SpiderType = Spider
StartRequestType = Iterable[RequestType]
