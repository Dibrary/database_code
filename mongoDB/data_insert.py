from pymongo import MongoClient

# client = MongoClient(host='localhost', port=27017)
client = MongoClient("mongodb://localhost:27017")

mydb = client['test'] # db이름

mycol = mydb['customers'] # collection 이름
my_dict = [{"name":"PUTTY","address":"SSH world"},
           {"name":"Avengers","address":"Avengers USA"}]
x = mycol.insert_many(my_dict)

print(x.inserted_ids)

'''
여기서 넣은 데이터는 mongoDB CLI 에서도 확인 가능
use test
db.customers.find() 하면 나온다.

'''