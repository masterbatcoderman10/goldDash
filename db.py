from sqlalchemy import Numeric, Date, create_engine, select, insert
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

    def __repr__(self):
        return f"GoldRates(pricedate={self.pricedate}, price22k={self.price22k}, price24k={self.price24k}, price18k={self.price18k})"


class Currencies(Base):

    __tablename__ = 'currencies'

    date = mapped_column(Date, primary_key=True)
    price = mapped_column(Numeric)

    def __repr__(self):
        return f"Currencies(date={self.date}, price={self.price})"


engine = create_engine(url, echo=True)

stmt = select(GoldRates)
insert_stmt = insert(GoldRates).values(pricedate='', price22k='', price24k='', price18k='')
counter = 5

with Session(engine) as session:
    for i, row in enumerate(session.execute(stmt)):
        print(row)
        if i == counter:
            break