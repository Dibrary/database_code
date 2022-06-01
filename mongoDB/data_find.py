from pymongo import MongoClient

# client = MongoClient(host='localhost', port=27017)
client = MongoClient("mongodb://localhost:27017")

mydb = client['test'] # db이름
mycol = mydb['customers'] # collection 이름
x = mycol.find_one()
print(x)


# 여러 개를 출력하려면
list = mycol.find()
for x in list:
    print(x)

