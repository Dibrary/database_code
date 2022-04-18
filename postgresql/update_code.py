import psycopg2

connector = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = '비밀번호')
cursor = connector.cursor()

sql = 'update sqlstudy.user set divide = %s where no = 2'

cursor.execute(sql, ("python",))
connector.commit()

print("데이터 수정 완료")


sql = 'select * from sqlstudy.user'

cursor.execute(sql, ())
values = cursor.fetchall()
print(values)

sql = 'update sqlstudy.user set divide = %s where no = 2'

cursor.execute(sql, ("technition",)) # 여기서 전달인자가 1개일 때 , 빼먹으면 안 된다.
connector.commit()
print("데이터 수정 완료")