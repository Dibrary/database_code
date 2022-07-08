from elasticsearch import Elasticsearch, helpers
from faker import Faker

fake = Faker()

es = Elasticsearch(['http://192.168.56.111:9200'])

def make_index(es, index_name):
    if es.indices.exists(index = index_name):
        es.indices.delete(index=index_name)
    print(es.indices.create(index=index_name))


index_name = 'goods'
make_index(es, index_name)

doc1 = {'goods_name':'노트북', 'price':100000}
doc2 = {'goods_name':'냉장고', 'price':150000}

es.index(index=index_name, doc_type='string', body=doc1)
es.index(index=index_name, doc_type='string', body=doc2)
es.indices.refresh(index=index_name)

# created 나오면 정상으로 입력된 것이다.





doc = {"name":fake.name(), "street":fake.street_address(), "city":fake.city(),
       "zip":fake.zipcode()}
res = es.index(index="users", doc_type="doc",body=doc)
print(res['result'])