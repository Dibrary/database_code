import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine("mysql+mysqldb://계정:비밀번호@ip:3306/데이터베이스이름")

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

Base.metadata.tables.keys() # 테이블 이름을 가져올 수 있다. (__tablename__로 정한 값)


