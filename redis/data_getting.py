import redis

conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

tmp_value = conn.get(1212)
print(tmp_value, type(tmp_value))
print(tmp_value.decode('utf-8'), type(tmp_value.decode('utf-8')))

print("가져오기 완료.")
