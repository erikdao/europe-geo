from typing import Optional

from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str = None
    slug: Optional[str] = None
    capital: str = None
    area: Optional[float] = None
    population: Optional[float] = None
    gdp_per_capita: Optional[float] = None
    internet_country_code: Optional[str] = None
    flag_file_name: Optional[str] = None


class CountryCreate(CountryBase):
    pass


class CountryUpdate(CountryBase):
    name: Optional[str] = None
    capital: Optional[str] = None


class Country(CountryBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
