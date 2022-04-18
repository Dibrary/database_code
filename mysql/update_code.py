import pymysql

connector = pymysql.connect(host='localhost', port=3306, db='testing', user='root', password='비밀번호', charset='utf8')
cursor = connector.cursor()

sql = 'update house_tb set network = %s where house_index = 12'
cursor.execute(sql, ('MODBUS',))

connector.commit()

print("데이터 수정 성공")