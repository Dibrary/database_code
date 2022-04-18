import psycopg2

connector = psycopg2.connect(host = 'localhost',database = 'postgres',user = 'postgres',password = '비밀번호')
cursor = connector.cursor()

sql = '''create table sqlstudy.user(
no integer not null primary key,
id varchar(40) not null,
divide varchar(40) not null);'''

cursor.execute(sql)
connector.commit() # commit 안 하면 테이블 생성 안됨.
print("테이블 생성 완료")


