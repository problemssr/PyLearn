# time模块
# 1. 时间戳
import time

t = time.time()
print(t)
# time.sleep(3)

t1 = time.time()
print(t1)

# 将时间戳转成字符串
s = time.ctime(t)
print(s)

# 将时间戳转成元组
t = time.localtime(t)
print(t)
print(t.tm_yday)
print(t.tm_hour)


# 将元组的转成时间戳
tt = time.mktime(t)
print(tt)

# 将元组的时间转成字符串
s = time.strftime('%Y-%m-%d %H:%M:%S')
print(s)

# 将字符串转成元组的方式
r = time.strptime('2019/06/20','%Y/%m/%d')
print(r)

'''
time模块：
重点:
  time()
  sleep()
  strftime('格式')   %Y  %m  %d  。。。。
了解：
  t = time.localtime(t)
  元组 ---》 t.tm_year   t.tm_mon  

'''