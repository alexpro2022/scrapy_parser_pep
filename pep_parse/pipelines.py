import csv
from datetime import datetime as dt
from collections import defaultdict

from pep_parse.typing import ItemType, SpiderType
from pep_parse.constants import (
    BASE_DIR, CSV_TITLE, DATETIME_FORMAT,
    DIALECT, ENCODING, EXT, RESULTS_DIR, TOTAL
)


class PepParsePipeline:

    def open_spider(self, spider: SpiderType) -> None:
        self.status_counter = defaultdict(int)

    def process_item(self, item: ItemType, spider: SpiderType) -> ItemType:
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider: SpiderType) -> None:
        filename = (
            f'status_summary_{dt.now().strftime(DATETIME_FORMAT)}.{EXT}')
        res_dir = BASE_DIR / RESULTS_DIR
        res_dir.mkdir(exist_ok=True)
        with open(res_dir / filename, 'w', encoding=ENCODING) as file:
            writer = csv.writer(file, dialect=DIALECT)
            writer.writerow(CSV_TITLE)
            writer.writerows(self.status_counter.items())
            writer.writerow((TOTAL, sum(self.status_counter.values())))
