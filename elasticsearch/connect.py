
from elasticsearch import Elasticsearch

es = Elasticsearch("http://192.168.56.113:9200/")
es.info()

