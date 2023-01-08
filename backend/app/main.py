from typing import Any, List

from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps, schemas, crud
from app.core.config import settings

app = FastAPI(openapi_url=f"{settings.API_V1_STR}/openapi.json")
router = APIRouter()


@router.get("/countries", response_model=List[schemas.Country])
def get_all_countries(db: Session = Depends(deps.get_db)) -> Any:
    return crud.country.get_multi(db)


@router.get("/countries/{slug}", response_model=schemas.Country)
def get_country_by_id(db: Session = Depends(deps.get_db), slug: str = None):
    return crud.country.get_by_slug(db, slug=slug)


app.include_router(router, prefix=settings.API_V1_STR)
