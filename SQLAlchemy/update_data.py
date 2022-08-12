
import datetime
from SQLAlchemy.create_table import User, session


session.query(User).filter_by(first = 1, second = 2, time = '2022-08-12 06:16:43').update({"first": "111", "second":"2222", "time":datetime.datetime.now()})
session.commit() # filter_by조건을 만족하는 row데이터를 update내용으로 업데이트한다.



