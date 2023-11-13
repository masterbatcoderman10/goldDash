from sqlalchemy import Numeric, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from script import *

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