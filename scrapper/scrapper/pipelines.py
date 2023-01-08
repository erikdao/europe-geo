# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class ScrapperPipeline:
    def process_item(self, item, spider):
        return item


class CustomFlagImageNamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'file_name': item['file_name']}) for x in item.get('image_urls')]
    
    def file_path(self, request, response=None, info=None, *, item=None):
        return request.meta['file_name']