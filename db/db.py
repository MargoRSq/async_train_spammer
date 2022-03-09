from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import MetaData
from utils.config import DATABASE_URL
from time import sleep

retries = 5
while (retries > 0):
    try:
        engine = create_engine(DATABASE_URL, echo=False)
        Base = declarative_base()
        metadata_obj = MetaData()

        Session = sessionmaker(bind=engine)
        session = Session()
        break
    except BaseException:
        retries-=1
        sleep(1)
    print(f"{retries} left")

