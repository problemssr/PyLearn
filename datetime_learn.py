# datetime: time模块升级版
'''
  datetime模块：
    time   时间
    date   日期     （data 数据）
    datetime  日期时间   now()
    timedelta  时间差  timedelta(days='',weeks ='' ,...)
'''
import datetime
import time

print(datetime.time.hour)  # 对象
print(time.localtime().tm_hour)

# 因为date是类，所以要求创建对象
d = datetime.date(2019, 6, 20)
print(d.day)
print(time.time())
print(datetime.date.ctime(d))

# datetime，timedelta
print(datetime.date.today())  # 2019-06-20

# 时间差
timedel = datetime.timedelta(days=3,hours=10)
print(timedel)

# datetime.datetime.now()  ---》 得到当前的日期和时间
now = datetime.datetime.now()
print(now)
result = now + timedel
print(result)

# 缓存： 数据redis  作为缓存   redis.set(key,value,时间差)  会话：session
