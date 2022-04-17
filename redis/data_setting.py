import redis

conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)
conn.set('test', 'hello world')

print("입력 완료.")
