import csv
import datetime as dt

from scrapy.exceptions import DropItem

from pep_parse.constants import DATETIME_FORMAT, RESULTS_DIR, RESULTS_PEP


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count_total = {
            'Active': 0,
            'Accepted': 0,
            'Deferred': 0,
            'Final': 0,
            'Provisional': 0,
            # 'Informational': 0,
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

        RESULTS_DIR.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = RESULTS_DIR / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(RESULTS_PEP)
