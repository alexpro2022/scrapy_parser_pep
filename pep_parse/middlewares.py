from scrapy import signals

from pep_parse.typing import (
    CrawlerType,
    ExceptionType,
    RequestType,
    ResponseType,
    ResultType,
    SpiderType,
    StartRequestType,
)


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: CrawlerType):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s  # type hint Self since Python 3.11 only

    def process_spider_input(
        self, response: ResponseType, spider: SpiderType
    ) -> None:
        return None

    def process_spider_output(
        self, response: ResponseType, result: ResultType, spider: SpiderType
    ) -> ResultType:
        for i in result:
            yield i

    def process_spider_exception(
        self, response: ResponseType,
        exception: ExceptionType, spider: SpiderType
    ) -> None:
        pass

    def process_start_requests(
        self, start_requests: StartRequestType, spider: SpiderType
    ) -> StartRequestType:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: SpiderType) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: CrawlerType):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(
        self, request: RequestType, spider: SpiderType
    ) -> None:
        return None

    def process_response(
        self, request: RequestType, response: ResponseType, spider: SpiderType
    ) -> ResponseType:
        return response

    def process_exception(
        self, request: RequestType,
        exception: ExceptionType, spider: SpiderType
    ) -> None:
        pass

    def spider_opened(self, spider: SpiderType) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
