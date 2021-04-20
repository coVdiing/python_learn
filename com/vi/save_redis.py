import redis
import coupon

pool = redis.ConnectionPool(host='113.31.118.233',port=6379,decode_responses=True)
r = redis.Redis(connection_pool=pool)

list = coupon.generate_coupon(200)

r.lpush('active_code',*list)
print(r.lrange('active_code',0,-1))