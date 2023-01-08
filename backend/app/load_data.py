"""
This script loads the country JSON data into the database
"""
import os
import json
from dotenv import load_dotenv

load_dotenv()

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from app import crud
from app.core.config import settings
from app.db.session import SessionLocal
from app.schemas.country import CountryCreate


def init() -> None:
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        return db
    except Exception as e:
        logger.error(e)
        raise e


def main():
    logger.info("Initializing db connection")
    db = init()

    logger.info("Get the list of countries' data files")
    json_files = sorted(
        [fn for fn in os.listdir(settings.COUNTRIES_DATA_DIR) if fn.endswith(".json")]
    )
    files = [os.path.join(settings.COUNTRIES_DATA_DIR, fn) for fn in json_files]

    for countr_file in files:
        with open(countr_file, "r") as f:
            data = json.load(f)
            obj_in = CountryCreate(**data)
            country = crud.country.create(db, obj_in=obj_in)
            logger.info(f"Added {country.name} to database")


if __name__ == "__main__":
    main()
