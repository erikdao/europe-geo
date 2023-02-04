from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Country(BaseModel):
    name: str
    official_name: str
    topLevelDomain: List[str]
    callingCode: str
    capital: str
    population: int
    area: int
    timezones: List[str]
    currencies: Optional[Dict[str, Any]]
    languages: Optional[Dict[str, str]]
    flag: Optional[str]


def transform_countries_data(raw_data: List[Any]) -> List[Country]:
    out_data = []
    for item in raw_data:
        item["flag"] = item["flag"]["large"]
        if not isinstance(item["topLevelDomain"], list):
            item["topLevelDomain"] = list(item["topLevelDomain"])
        out_data.append(Country.parse_obj(item))

    return out_data
