import json
from typing import Any
from scrapy.http import Response
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider

from items import MelodybrazilItem


class CrawMelody(SitemapSpider):
    name = "melodybrazil_crawler"
    allowed_domains = ["melodybrazil.com"]
    sitemap_urls = ["https://www.melodybrazil.com/robots.txt"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        script = response.xpath('//script[@type="application/ld+json"][1]/text()').get()
        data = json.loads(script)

        item_loader = ItemLoader(item=MelodybrazilItem(), response=response)
        item_loader.add_value('author', data.get('author')['name'])
        item_loader.add_value('url', data.get('mainEntityOfPage').get('@id'))
        item_loader.add_value('name', data.get('headline'))
        item_loader.add_value('date_published', data.get('datePublished'))
        item_loader.add_xpath('url_download', xpath='//a[@data-download-count="true"]/@onclick')

        yield item_loader.load_item()
