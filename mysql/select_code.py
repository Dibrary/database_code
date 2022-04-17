import pymysql


connector = pymysql.connect(host='localhost', port=3306, db='practice', user='root', password='비밀번호', charset='utf8')
cursor = connector.cursor()

sql = 'SELECT * from book'
cursor.execute(sql)
values = cursor.fetchall()

print(values, len(values), type(values))