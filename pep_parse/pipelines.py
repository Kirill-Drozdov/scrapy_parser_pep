import csv
import datetime as dt
from pathlib import Path

from scrapy.exceptions import DropItem

from pep_parse.constants import DATETIME_FORMAT, RESULTS_PEP, FILE_NAME

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count_total = {
            'Active': 0,
            'Accepted': 0,
            'Deferred': 0,
            'Final': 0,
            'Provisional': 0,
            'Rejected': 0,
            'Superseded': 0,
            'Withdrawn': 0,
            'Draft': 0,
            'Total': 0
        }

    def process_item(self, item, spider):
        status = item['status']
        try:
            self.status_count_total[status] += 1
            self.status_count_total['Total'] += 1
        except KeyError:
            raise DropItem(f'Несуществующий статус: {status}')

        return item

    def close_spider(self, spider):
        for status, count_status in self.status_count_total.items():
            RESULTS_PEP.append((status, count_status))
        RESULTS_DIR = BASE_DIR / 'results'
        RESULTS_DIR.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_path = RESULTS_DIR / FILE_NAME.format(now_formatted)

        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix', quoting=csv.QUOTE_NONE)
            writer.writerows(RESULTS_PEP)
