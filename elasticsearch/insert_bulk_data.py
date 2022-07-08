from elasticsearch import Elasticsearch, helpers
from faker import Faker

fake = Faker()

es = Elasticsearch(['http://192.168.56.111:9200'])

actions = []
for x in range(98):
    actions.append({
    "_index":"users",
    "_type":"doc",
    "_source":{
        "name":fake.name(),
        "street":fake.street_address(),
        "city":fake.city(),
        "zip":fake.zipcode()
    }
})

res = helpers.bulk(es, actions)
# print(res['result']) # TypeError: tuple indices must be integers or slices, not str 이런 에러가 난다.
print(res) # 출력은 (98, []) 으로 나온다.



