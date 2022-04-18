import pymysql

connector = pymysql.connect(host='localhost', port=3306, db='testing', user='root', password='비밀번호', charset='utf8')
cursor = connector.cursor()

sql = 'delete from analyzer_event_tb where no = %s'
cursor.execute(sql, (678,))

connector.commit()

print("데이터 삭제 성공")