from typing import TypeAlias

from scrapy.http import Response

from .items import PepParseItem

ItemType: TypeAlias = PepParseItem
ResponseType: TypeAlias = Response
