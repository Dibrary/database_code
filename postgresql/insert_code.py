import psycopg2

connector = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = '비밀번호')
cursor = connector.cursor()

sql = '''insert into sqlstudy.user(no,id,divide) values(%s,%s,%s)'''

cursor.execute(sql, (2, 'raffia','technition'))
connector.commit() # commit 안 하면 데이터가 커서에만 남아있음. 실제 DB서버에 반영하려면 필수.
print("데이터 입력 완료")


