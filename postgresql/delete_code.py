import psycopg2

connector = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = '비밀번호')
cursor = connector.cursor()

sql = 'delete from sqlstudy.user where no = %s'

cursor.execute(sql, (2,))
connector.commit()

print("데이터 삭제 완료")
