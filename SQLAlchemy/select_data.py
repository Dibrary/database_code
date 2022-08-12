
from SQLAlchemy.create_table import User, session

result = session.query(User).filter_by(first = 1, second = 2) # first가 1이고, second가 2인 조건을 만족하는 데이터 가져옴.
type(result) # 이 결과는 sqlalchemy.orm.query.Query

for k in result:
    print(k) # 이렇게 하면 해당 데이터가 나온다. tuple처럼 보이지만, User 객체다.



query = session.query(User).filter(User.first == 111).order_by(User.first) # 이렇게도 가져올 수 있다.
query.all() # first가 111이고, first로 정렬한 데이터 모두 가져오기.

query.first() # 이 코드는 첫 번째 값만 가져온다. 즉 select 에 limit 1 을 적용한 셈.




for user in session.query(User).filter(User.first < 224).order_by(User.first).all():
    print(user.first, user)
# 위 코드 방식으로 한 번에 다 가져올 수도 있다. (first가 224보다 작고, first를 순서대로 정렬.

