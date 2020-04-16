import pymysql
from redis import StrictRedis
# 连接mysql
db = pymysql.connect('localhost', 'root', '', 'db_test')
mysql = db.cursor()
# print(mysql)
# sql="insert into t_python(name,type) values (%s,%s)"
# mysql.execute(sql,('okc',0))
# sql=mysql.execute('insert into t_python()')
db.commit()
# select = mysql.execute("select * from t_python")
# data = mysql.fetchall()
# print(data)

# # 连接redis
# redis = StrictRedis(host='localhost', port='6379', db=0, password='')
# # redis.set('name', 'Leo')
# # print(redis.get('name'))
# redis.mset(k1='v1', k2='v2', k3='abcdefg')
# redis.set('num', 100)
# # print(redis.mget("k1"))
# # print(redis.getrange('k3', 0, 2))
# # redis.setrange('k3',1,'hct')
# # print(redis.strlen('k3'))
# # print(redis.incr('num'))
# # print(redis.decr('num', 20))
# redis.append('k3', 'dadada')
# print(redis.get('k3'))
