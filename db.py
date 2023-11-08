from sqlalchemy import Numeric, Date, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('PSQL_URL')

class Base(DeclarativeBase):
    pass

class GoldRates(Base):

    __tablename__ = 'goldrates'

    pricedate = mapped_column(Date, primary_key=True)
    price22k = mapped_column(Numeric)
    price24k = mapped_column(Numeric)
    price18k = mapped_column(Numeric)


class Currencies(Base):

    __tablename__ = 'currencies'

    date = mapped_column(Date, primary_key=True)
    price = mapped_column(Numeric)


engine = create_engine(url, echo=True)

stmt = select(GoldRates)
counter = 5

with Session(engine) as session:
    for i, row in enumerate(session.execute(stmt)):
        print(row)
        if i == counter:
            break