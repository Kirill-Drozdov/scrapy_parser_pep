from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):
    header_map = {'number': 'Номер',
                  'name': 'Название',
                  'status': 'Статус'}

    def _write_headers_and_set_fields_to_export(self, item):
        if not self.include_headers_line:
            return
        if not self.fields_to_export:
            if isinstance(item, dict):
                self.fields_to_export = list(item.keys())
            else:
                self.fields_to_export = list(item.fields.keys())
        headers = list(self._build_row(self.fields_to_export))

        headers = [self.header_map.get(header, header) for header in headers]
        self.csv_writer.writerow(headers)
