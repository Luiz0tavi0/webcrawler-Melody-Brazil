import html
from datetime import datetime, timezone

import xlwt
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings


class CleanDataPipeline:
    def process_item(self, item, spider):
        # Limpar espaços em branco
        for key, value in item.items():
            if isinstance(value, str):
                item[key] = value.strip()

        # Decodificar caracteres HTML
        for key, value in item.items():
            if isinstance(value, str):
                item[key] = html.unescape(value)

        return item


class MelodybrazilTransformPipeline:
    def process_item(self, item, spider):
        self.convert_date_to_utc(item)
        return item

    @staticmethod
    def convert_date_to_utc(item):
        dt_publishied = datetime.fromisoformat(item['date_published'])

        dt_publishied_utc = dt_publishied.astimezone(timezone.utc)

        item['date_published'] = dt_publishied_utc.replace(tzinfo=None)  # Remove o deslocamento da hora


class MelodybrazilLoadPipeline:
    def __init__(self):
        self.settings = get_project_settings()
        self.workbook = None
        self.sheet = None
        self.headers_names = ['URL', 'NOME', 'DATA UTC', 'Publicado Por', 'URL DE DOWNLOAD']
        self.row_index = 0
        self.datetime_style = xlwt.XFStyle()
        self.datetime_style.num_format_str = 'DD/MM/YYYY HH:MM:SS'

    def process_item(self, item, spider):
        spider.logger.info(f"PROCESSANDO: {item['name']}")
        adapter = ItemAdapter(item)

        self.sheet.write(self.row_index, 0, adapter['url'])
        self.sheet.write(self.row_index, 1, adapter['name'])
        self.sheet.write(self.row_index, 2, adapter['date_published'], self.datetime_style)
        self.sheet.write(self.row_index, 3, adapter['author'])
        self.sheet.write(self.row_index, 4, adapter.get('url_download', 'Link Inválido'))
        #
        self.row_index += 1
        if self.row_index % 1000 == 0:
            spider.logger.info(f"Persistência Intermediária em {self.settings.get('XLS_FILE_OUTPUT')}")
            self.workbook.save(self.settings.get('XLS_FILE_OUTPUT'), )

    def open_spider(self, item):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workbook.add_sheet(self.settings.get('SHEET_NAME'), cell_overwrite_ok=True)

        for col, column_name in enumerate(self.headers_names):
            self.sheet.write(self.row_index, col, column_name)
        self.row_index += 1
        self.workbook.save(self.settings.get('XLS_FILE_OUTPUT'), )

    def close_spider(self, spider):
        spider.logger.info(f"FINALIZANDO SPIDER.")
        self.workbook.save(self.settings.get('XLS_FILE_OUTPUT'), )
