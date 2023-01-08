from fastapi import FastAPI

from app.core.config import settings
from app.schemas.country import Country

app = FastAPI()

countries = [
    {
        "name": "France",
        "area": 643801.0,
        "population": 68305148.0,
        "capital": "Paris",
        "gdp_per_capita": 42000.0,
        "internet_country_code": "metropolitan France - .fr; French Guiana - .gf; Guadeloupe - .gp; Martinique - .mq; Mayotte - .yt; Reunion - .re",
        "flag_file_name": "250px-Flag_of_France.svg.png"
    },
    {
        "name": "Sweden",
        "area": 450295.0,
        "population": 10483647.0,
        "capital": "Stockholm",
        "gdp_per_capita": 50700.0,
        "internet_country_code": ".se",
        "flag_file_name": "255px-Flag_of_Sweden.svg.png"
    }
]

@app.get("/")
async def root():
    out = [Country(**item) for item in countries]
    return out    
