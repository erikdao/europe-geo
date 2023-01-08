# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class CountryItem(Item):
    name = Field()
    capital = Field()
    area = Field()
    population = Field()
    gdp_per_capita = Field()
    country_url = Field()
    internet_country_code = Field()


class FlagItem(Item):
    file_name = Field()
    image_urls= Field()