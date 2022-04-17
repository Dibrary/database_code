import pymysql

connector = pymysql.connect(host='localhost', port=3306, user='root', password='비밀번호', charset='utf8')

cursor = connector.cursor()

sql = 'create database testing_tb'
# 삭제할 때는 sql = 'drop database testing_tb'

cursor.execute(sql)

print("테이블 생성 완료")