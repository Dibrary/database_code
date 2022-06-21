
from elasticsearch import Elasticsearch
from faker import Faker

es = Elasticsearch({'192.168.56.113:9200/'})
es.info()


