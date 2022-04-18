import psycopg2

connector = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = '비밀번호')
cursor = connector.cursor()

sql = '''select * from sqlstudy.user'''

cursor.execute(sql, ())
values = cursor.fetchall()

print(values, type(values), values[0])
print("데이터 검색 완료")
