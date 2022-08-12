
from SQLAlchemy.create_table import User, session

session.query(User).filter_by(first = 2, second=3).delete() # first가 2이고 second가 3인 데이터를 삭제한다.
session.commit()

