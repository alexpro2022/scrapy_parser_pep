import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.constants import (BASE_DIR, CSV_TITLE, DATETIME_FORMAT,
                                 ENCODING, EXT, RESULTS_DIR, TOTAL)
from pep_parse.typing import ItemType, SpiderType


class PepParsePipeline:

    def open_spider(self, spider: SpiderType) -> None:
        self.status_counter = defaultdict(int)

    def process_item(self, item: ItemType, spider: SpiderType) -> ItemType:
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider: SpiderType) -> None:
        res_dir = BASE_DIR / RESULTS_DIR
        # res_dir.mkdir(exist_ok=True)
        filename = (
            f'status_summary_{dt.now().strftime(DATETIME_FORMAT)}.{EXT}')
        with open(res_dir / filename, 'w', encoding=ENCODING) as file:
            csv.writer(file, dialect=csv.unix_dialect).writerows((
                CSV_TITLE,
                *self.status_counter.items(),
                (TOTAL, sum(self.status_counter.values())),
            ))
