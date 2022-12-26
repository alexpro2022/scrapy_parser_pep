import csv
from datetime import datetime as dt

from .constants import BASE_DIR, DATETIME_FORMAT, ENCODING


class PepParsePipeline:
    status_counter = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_counter[status] = self.status_counter.get(status, 0) + 1
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        filename = f'status_summary_{dt.now().strftime(DATETIME_FORMAT)}.csv'
        path = BASE_DIR / filename
        with open(path, 'w', encoding=ENCODING) as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(self.status_counter.items())
            writer.writerow(('Total', sum(self.status_counter.values())))
