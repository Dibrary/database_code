import pymysql

connector = pymysql.connect(host='localhost', port=3306, db='practice', user='root', password='비밀번호', charset='utf8')
cursor = connector.cursor()

sql = 'INSERT INTO book(id, divided_no, bookname, writer, publisher) values(%s,%s,%s,%s,%s)'
cursor.execute(sql, ('1','325.04','플렛폼제국의 성공 시나리오','다나카 미치아키','이너북'))

connector.commit()

print("데이터 삽입 성공")