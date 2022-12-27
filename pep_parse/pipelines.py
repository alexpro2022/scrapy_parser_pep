import csv
from datetime import datetime as dt

from pep_parse.typing import ItemType, SpiderType
from pep_parse.constants import (
    BASE_DIR, CSV_TITLE, DATETIME_FORMAT, DIALECT, ENCODING, EXT, TOTAL)


class PepParsePipeline:
    status_counter = {}

    def process_item(self, item: ItemType, spider: SpiderType) -> ItemType:
        status = item['status']
        self.status_counter[status] = self.status_counter.get(status, 0) + 1
        return item

    def open_spider(self, spider: SpiderType) -> None:
        pass

    def close_spider(self, spider: SpiderType) -> None:
        filename = (
            f'status_summary_{dt.now().strftime(DATETIME_FORMAT)}.{EXT}')
        with open(BASE_DIR / filename, 'w', encoding=ENCODING) as file:
            writer = csv.writer(file, dialect=DIALECT)
            writer.writerow(CSV_TITLE)
            writer.writerows(self.status_counter.items())
            writer.writerow((TOTAL, sum(self.status_counter.values())))
