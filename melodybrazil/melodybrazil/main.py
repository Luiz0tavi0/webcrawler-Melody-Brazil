from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.spyder_page import CrawMelody


process = CrawlerProcess(get_project_settings())

if __name__ == '__main__':
    process.crawl(CrawMelody)

    # Execute o processo do rastreador
    process.start()


