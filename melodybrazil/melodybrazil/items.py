# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

from urllib.parse import urlparse


def get_path(url):
    parsed_url = urlparse(url)
    relative_path = parsed_url.path
    return relative_path


def clean_str(s): return remove_tags(s).strip()


def extract_url_download(url): return re.findall(pattern=r"href='(.*?)'", string=url)


class MelodybrazilItem(scrapy.Item):
    url = scrapy.Field(
        input_processor=MapCompose(get_path, clean_str, str.lower),
        output_processor=TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(clean_str, ),
        output_processor=TakeFirst()
    )
    date_published = scrapy.Field(
        input_processor=MapCompose(clean_str, ),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(clean_str, ),
        output_processor=TakeFirst()
    )
    url_download = scrapy.Field(
        input_processor=MapCompose(extract_url_download, clean_str, str.lower),
        output_processor=TakeFirst()
    )
