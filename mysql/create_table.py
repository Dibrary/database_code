import pymysql

connector = pymysql.connect(host='localhost', port=3306, db='practice', user='root', password='비밀번호', charset='utf8')
cursor = connector.cursor()

sql = '''
CREATE TABLE book(
id int(10) not null auto_increment,
divided_no varchar(40) not null,
bookname varchar(40) not null,
writer varchar(40) not null,
publisher varchar(40) not null,
primary key(id));
'''

cursor.execute(sql)

print("테이블 생성 완료")


