from elasticsearch import Elasticsearch

es = Elasticsearch("http://192.168.56.113:9200/")

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