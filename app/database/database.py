from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from config.config import settings


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#while True:
#   try:
#        conn = psycopg2.connect(host = 'localhost', database= 'africatradetoday', user = 'postgres', password = 'Judithida1', cursor_factory= RealDictCursor)
#        cursor = conn.cursor()
#        print("Database connection succesfull")
#        break
#    except Exception as error:
#        print("Connection to database failed")
#        print("Error: ", error)
#        time.sleep(2)
    
SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:Judithida1@localhost/africatradetoday'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

