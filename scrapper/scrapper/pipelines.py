# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import json
from pathlib import Path
from locale import atof, setlocale, LC_NUMERIC
setlocale(LC_NUMERIC, 'en_US.ISO8859-1')

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

current_path = Path(os.path.dirname(__file__))
data_path = current_path / "data"


class CountryItemPipeline:
    def process_item(self, item, spider):
        # Convert string to numbers for some attributes
        out_item = {
            "name": item["name"],
            "area": self._process_item_area(item),
            "population": self._process_item_population(item),
            "capital": item["capital"],
            "gdp_per_capita": self._process_item_gdp_per_capita(item),
        }

        file_name = item["country_url"] + ".json"
        with open(data_path / file_name, "w") as f:
            json.dump(out_item, f, indent=2)

    def _process_item_area(self, item) -> float:
        s = item.get("area", "")
        s = s.split(" ")[0].strip()
        return atof(s)

    def _process_item_population(self, item) -> float:
        s = item.get("population", "")
        s = s.split(" ")[0].strip()
        return atof(s)

    def _process_item_gdp_per_capita(self, item) -> float:
        s = item.get("gdp_per_capita", "")
        s = s.split(" ")[0].strip()
        if s.startswith("$"):
            s = s.replace("$", "")
        return atof(s)

class CustomFlagImageNamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'file_name': item['file_name']}) for x in item.get('image_urls')]
    
    def file_path(self, request, response=None, info=None, *, item=None):
        return request.meta['file_name']