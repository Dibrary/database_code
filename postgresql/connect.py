import psycopg2 as db

conn_string = "dbname='dataengineering' host='localhost' user='postgres' " \
              "password='비밀번호'"
conn = db.connect(conn_string)
cur = conn.cursor()

query = "insert into users(id, name, street, city, zip) values({},{},{},{},{})".format(1, 'Big Bird', 'Sesame Street', 'Fakeville', '12345')
cur.mogrify(query)

query2 = "insert into users (id, name, street, city, zip) values(%s,%s,%s,%s,%s)"
data = (2, 'Small Bird', 'Sesame Street', 'Fakeville', '12345')

# cur.mogrify(query2, data)
cur.execute(query2,data)

conn.commit()