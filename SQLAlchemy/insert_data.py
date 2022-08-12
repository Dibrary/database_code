
from SQLAlchemy.create_table import User, session

user = User(1, 2)
session.add(user)
session.commit() # 이렇게 하면 데이터 들어간다.





