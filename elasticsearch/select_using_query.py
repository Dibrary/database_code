
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(['http://192.168.56.111:9200'])

res = es.search(index='users',
                doc_type='doc',
                scroll='20m',
                size=500,
                body={"query":{"match_all":{}}})

print(res)

sid = res['_scroll_id']
size = res['hits']['total']

while (size > 0):
    res = es.scroll(scroll_id = sid, scroll='20m')

    sid = res['_scroll_id']
    size = len(res['hits']['hits'])

    for doc in res['hits']['hits']:
        print(doc['_source'])

