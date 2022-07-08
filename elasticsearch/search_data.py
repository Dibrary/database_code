
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(['http://192.168.56.111:9200'])

doc = {"query":{"match_all":{}}}
res = es.search(index="users", body=doc, size=10)

for k in res['hits']['hits']:
    print(k)

# print(res['hits']['hits'])
print("=============================================")

from pandas.io.json import json_normalize
df = json_normalize(res['hits']['hits'])
doc = {"query":{"match":{"name":"James Hoffman"}}}
res = es.search(index="users", body=doc, size=10)
print(res['hits']['hits'][0]['_source'])

