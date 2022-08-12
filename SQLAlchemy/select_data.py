
from SQLAlchemy.create_table import User, session

result = session.query(User).filter_by(first = 1, second = 2) # first가 1이고, second가 2인 조건을 만족하는 데이터 가져옴.
type(result) # 이 결과는 sqlalchemy.orm.query.Query

for k in result:
    print(k) # 이렇게 하면 해당 데이터가 나온다. tuple처럼 보이지만, User 객체다.