import os
import json
import logging
from typing import Any, List

from dotenv import load_dotenv
load_dotenv()

import click
import requests
from requests.exceptions import HTTPError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_ENDPOINT = "https://countryapi.io/api/all"


def get_eu_countries_data() -> List[Any]:
    headers = {"Authorization": f"Bearer {os.environ['COUNTRY_API_KEY']}"}
    try:
        response = requests.get(API_ENDPOINT, headers=headers)
        data = response.json()

        # For now, we only take countries in Europe
        eu_countries = [item for _, item in data.items() if item["region"] == "Europe"]
        logger.info(f"Got data for {len(eu_countries)} countries in Europe")
        return eu_countries
    except HTTPError as ex:
        logger.error(ex)


def download_flag_images(urls: List[str], output_dir: Any) -> None:
    pass


@click.command()
@click.option(
    "--output-dir",
    type=str,
    required=False,
    default="data/",
    help="Directory storing output data"
)
def main(output_dir) -> None:
    countries = get_eu_countries_data()
    
    with open(os.path.join(output_dir, "countries.json"), "w") as f:
        json.dump(countries, f, indent=2)
    logger.info("Wrote countries data files!")


if __name__ == "__main__":
    main()
