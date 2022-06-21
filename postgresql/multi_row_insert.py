
import psycopg2 as db
from faker import Faker
from connect import cur, conn

fake = Faker()
data = []
i = 2

for i in range(100):
    data.append((i, fake.name(), fake.street_address(), fake.zipcode(), fake.city())) # for문으로 한 번에 구성하고
    i += 1

data_for_db = tuple(data) # tuple로 변환

query = "insert into users (id, name, street, zip, city) values(%s,%s,%s,%s,%s)"
cur.executemany(query, data_for_db) # executemany를 써서 한 번에 넣을 수 있다.
conn.commit()


