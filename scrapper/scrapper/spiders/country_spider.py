import os
from pathlib import Path

import scrapy
from scrapper.items import CountryItem

current_path = Path(os.path.dirname(__file__))
project_root = current_path.parent
data_path = os.path.join(project_root, "data")


class CountrySpider(scrapy.Spider):
    name = "countries"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapper.pipelines.CountryItemPipeline': 100
        }
    }

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.base_xpath = "//div[contains(concat(' ', normalize-space(@class), ' '), 'content-area-content')]/"

        self.base_url = "https://www.cia.gov/the-world-factbook/countries/"
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
            url = self.base_url + key.lower()
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(country_url=key, country=value))
    
    def parse(self, response, **kwargs):
        country = kwargs.get("country", None)
        country_url = kwargs.get("country_url", None)

        xpath_dict = {
            "area": 'div[@id="geography"]/div[4]/p/text()',
            "population": 'div[@id="people-and-society"]/div[1]/p/text()',
            "capital": 'div[@id="government"]/div[3]/p/text()',
            "gdp_per_capita": 'div[@id="economy"]/div[4]/p/text()'
        }

        country_item = CountryItem()
        country_item["name"] = country
        country_item["country_url"] = country_url.replace("-", "_")

        for key, value in xpath_dict.items():
            xp = "".join([self.base_xpath, value])
            text = response.xpath(xp).extract_first()
            country_item[key] = text.strip() if text is not None else text
        
        return country_item
