
from elasticsearch import Elasticsearch
from faker import Faker

es = Elasticsearch(['http://192.168.56.111:9200']) # 파이썬 elasticsearch 모듈 버전과 실제 일래스틱서치 서버 버전을 맞춰야 함.
print(es.info())

