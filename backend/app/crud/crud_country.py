from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.country import Country
from app.schemas.country import CountryCreate


class CRUDCountry(CRUDBase[Country, CountryCreate]):
    def create(self, db: Session, *, obj_in: CountryCreate) -> Country:
        return super().create(db, obj_in=obj_in)


country = CRUDCountry(Country)
