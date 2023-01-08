import os
import json
from pathlib import Path

import scrapy
from scrapper.items import FlagItem

current_path = Path(os.path.dirname(__file__))
project_root = current_path.parent
data_path = os.path.join(project_root, "data", "images")


class FlagSpider(scrapy.Spider):
    name = "flags"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapper.pipelines.CustomFlagImageNamePipeline': 200
        }
    }

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

        self.base_url = "https://en.wikipedia.org/wiki/Flag_of_"
        self.countries = {
            'armenia': 'Armenia',
            'albania': 'Albania',
            'andorra': 'Andorra',
            'austria': 'Austria',
            'belarus': 'Belarus',
            'belgium': 'Belgium',
            'bosnia-and-herzegovina': 'Bosnia and Herzegovina',
            'bulgaria': 'Bulgaria',
            'croatia': 'Croatia',
            'cyprus': 'Cyprus',
            'czechia': 'Czech Republic',
            'denmark': 'Denmark',
            'estonia': 'Estonia',
            'finland': 'Finland',
            'france': 'France',
            'germany': 'Germany',
            'georgia': 'Georgia',
            'greece': 'Greece',
            'hungary': 'Hungary',
            'iceland': 'Iceland',
            'ireland': 'Ireland',
            'italy': 'Italy',
            'kosovo': 'Kosovo',
            'latvia': 'Latvia',
            'liechtenstein': 'Liechtenstein',
            'lithuania': 'Lithuania',
            'luxembourg': 'Luxembourg',
            'malta': 'Malta',
            'moldova': 'Moldova',
            'monaco': 'Monaco',
            'montenegro': 'Montenegro',
            'netherlands': 'Netherlands',
            'norway': 'Norway',
            'poland': 'Poland',
            'portugal': 'Portugal',
            'romania': 'Romania',
            'russia': 'Russia',
            'san-marino': 'San Marino',
            'serbia': 'Serbia',
            'slovakia': 'Slovakia',
            'slovenia': 'Slovenia',
            'spain': 'Spain',
            'sweden': 'Sweden',
            'switzerland': 'Switzerland',
            'turkey': 'Turkey',
            'ukraine': 'Ukraine',
            'united-kingdom': 'United Kingdom'
        }
    
    def start_requests(self):
        for key, value in self.countries.items():
            country_suffix = value.replace(" ", "_")
            url = "".join([self.base_url, country_suffix])
            # Special surgery for Georgia
            if key == "georgia":
                url += "_(country)"

            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(country_url=key, country=value))
        
    def parse(self, response, **kwargs):
        country_url = kwargs.get("country_url", None)

        # Get the img tag of the flag
        xp = '//*[@id="mw-content-text"]//img[@class="thumbborder"]/@src'
        flag_url = response.xpath(xp).get()

        flag_item = FlagItem()
        flag_item['image_urls'] = ["https:" + flag_url.strip()]
        flag_item['file_name'] = flag_url.split("/")[-1]

        if "-" in country_url:
            country_url = country_url.replace("-", "_")
    
        with open(os.path.join(os.path.dirname(data_path), country_url + ".json"), "r") as f:
            data = json.load(f)
        data["flag_file_name"] = flag_item['file_name']
        with open(os.path.join(os.path.dirname(data_path), country_url + ".json"), "w") as f:
            json.dump(data, f, indent=2)

        return flag_item
