import os
import json
from typing import List
from pathlib import Path

module_path = Path(os.path.abspath(__file__))
app_path = module_path.parent
project_root = app_path.parent

from fastapi import FastAPI
from app.schemas import Country, transform_countries_data

app = FastAPI()


def get_coutries_data():
    with open(project_root / "data" / "countries.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
async def get_countries() -> List[Country]:
    return transform_countries_data(get_coutries_data())
