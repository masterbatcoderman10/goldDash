import logging
from sqlalchemy import Numeric, Date, create_engine, select, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from dotenv import load_dotenv
from script import *
from db_tables import *
import os
import time

# Set up logging
logging.basicConfig(filename='logs.txt', level=logging.INFO)

load_dotenv()

url = os.getenv('PSQL_URL')
date = dt.datetime.now().date()
logging.info(f'------------------------------------------')
logging.info(f'DATE: {date}')
logging.info('\n\n\n')
start = time.time()
logging.info('Getting data')
prices, currency = get_data(init_driver())
logging.info('Fetched data')
price22k = prices[1]
price24k = prices[0]
price18k = prices[2]

engine = create_engine(url, echo=True)

stmt = select(GoldRates)
counter = 5
# Making update
logging.info('Making update')
with Session(engine) as session:
    todays_gold_rate = GoldRates(
        pricedate=date,
        price22k=price22k,
        price24k=price24k,
        price18k=price18k
    )
    
    todays_currency = Currencies(
        date=date,
        price=currency
    )
    
    session.add_all([todays_gold_rate, todays_currency])
    session.commit()

end = time.time()
logging.info(f"Script took {end - start} seconds to run")
logging.info('\n\n\n')
logging.info('------------------------------------------')