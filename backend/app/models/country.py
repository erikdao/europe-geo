from sqlalchemy import Column, Integer, String, Numeric

from app.db.base_class import Base


class Country(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    capital = Column(String, nullable=False)
    area = Column(Numeric(10, 2, decimal_return_scale=None, asdecimal=False),)
    population = Column(Numeric(10, 2, decimal_return_scale=None, asdecimal=False),)
    gdp_per_capita = Column(Numeric(10, 2, decimal_return_scale=None, asdecimal=False),)
    internet_country_code = Column(String, nullable=True)
    flag_file_name = Column(String, nullable=True)
