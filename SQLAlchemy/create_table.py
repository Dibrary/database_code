

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine("mysql+mysqldb://계정:비밀번호@ip:3306/데이터베이스이름")

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__="IMPT"
    first = Column(Integer)
    # first = Column(Integer, primary_key=True) # PK 지정하려면 이렇게 하면 됨.
    second = Column(Integer)
    time = Column(DateTime, default=datetime.datetime.utcnow, primary_key=True)

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "< (%s, %s) >"%(self.first, self.second)

Base.metadata.create_all(engine) # 이 코드를 작성해야 DB에 들어간다.
# Base.metadata.drop_all(engine) # 이 코드를 실행하면 해당 DB 삭제됨.



