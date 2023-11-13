from sqlalchemy import Numeric, Date, create_engine, select, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from dotenv import load_dotenv
from script import *
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


date, prices, currency = get_data(init_driver())
price22k = float(prices[1])
price24k = float(prices[0])
price18k = float(prices[2])


engine = create_engine(url, echo=True)

stmt = select(GoldRates)
counter = 5
#Making update
print('making update')
with Session(engine) as session:
    # for i, row in enumerate(session.execute(stmt)):
    #     print(row)
    #     if i == counter:
    #         break

    todays_gold_rate = GoldRates(
        pricedate=date,
        price22k=price22k,
        price24k=price24k,
        price18k=price18k
    )
    
    todays_currency = Currencies(
        date=date,
        price=float(currency)
    )
    
    session.add_all([todays_gold_rate, todays_currency])
    session.commit()
