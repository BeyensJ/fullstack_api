from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://<user>:<passwork>@<host>:3306/<dbname>"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={
        'ssl': {"rejectUnauthorized": 'false'}}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
