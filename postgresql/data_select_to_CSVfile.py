from connect import conn,cur

query = "select * from users"
cur.execute(query)

# print(cur.rowcount) # 몇 개 있는지 알 수 있음.

# for record in cur:
#     print(record, type(record), cur.rownumber) # cur.rownumber로 현재 번호까지 같이 알 수 있음.

f = open('fromdb.csv', 'w')
cur.copy_to(f, 'users', sep=',')
f.close()

f = open('fromdb.csv', 'r')
print(f.read())


'''
cur.fetchall()
cur.fetchmany(10)
cur.fetchone()
'''