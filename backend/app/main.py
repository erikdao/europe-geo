import os
import json
from typing import List
from pathlib import Path

module_path = Path(os.path.abspath(__file__))
app_path = module_path.parent
project_root = app_path.parent

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import Country, transform_countries_data

app = FastAPI()
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTION"],
    allow_headers=["*"]
)
router = APIRouter()

def get_coutries_data():
    with open(project_root / "data" / "countries.json", "r") as f:
        data = json.load(f)
    return data


@router.get("/countries", response_model=List[Country])
async def get_countries() -> List[Country]:
    return transform_countries_data(get_coutries_data())


app.include_router(router, prefix="/api/v1")
