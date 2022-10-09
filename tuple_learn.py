'''
总结列表:
list
1. 定义

l = [] 空列表
l = ['aaa']

2.符号：
+   ----》 合并 []+[]
*  ----->  [] * n
in  ----> a in [] False True
not in ---->
is  地址是否相等
not is


3.系统中给列表用函数：
len(list) ----> int
sorted(list)  ----> 排序
max()  最大值
min()  最小值
list()  强制转换成列表类型
enumerate(list) 枚举  index  value

4. 列表自身函数:
添加元素:
   append()   末尾添加
   extend()   末尾添加一组元素
   insert()   指定位置插入

删除:
    del list1[index]

    remove(obj)  删除指定的元素，如果指定的元素不存在则报异常

    pop()  队列  FIFO   栈  FILO  默认删除的是最后一个元素

    clear() 清空元素

其他:
    count()   指定元素的个数
    sort()    排序
    reverse()  翻转   [4,6,8,9,0]  --->  [0,9,8,6,4]

算法:
   选择排序
   冒泡排序
'''

'''
 元组：
 类似列表（当成容器）
 特点：
 1. 定义的符号：()  
 2. 元组中的内容不可修改
 3. 关键字: tuple   

    列表                 元组

    []                  （）
    [1]                  (1,)
    [1,2]                (1,2)
'''

t1 = ()
print(type(t1))  # <class 'tuple'>

t2 = ('hello',)
print(type(t2))

t3 = ('aa', 'bb')
print(type(t3))

#
t4 = (3, 5, 7, 8, 1, 4, 7, 8, 9, 0)

# 增删改  查

import random

list1 = []

for i in range(10):
    ran = random.randint(1, 20)

    list1.append(ran)

print(list1)  #

# tuple()
# list()
t5 = tuple(list1)
print(t5)

# 查询： 下标index  切片 [:]
print(t5[0])
print(t5[-1])

print(t5[2:-3])
print(t5[::-1])

# 最大值  最小值

print(max(t5))
print(min(t5))

# 求和
print(sum(t5))

# 求长度
print(len(t5))

# 元组中的函数：
# index(obj)  ---》 个数
# count(obj)  ---》 下标位置

print(t5.count(4))  # 个数

print(t5.index(4))  # 从t5这个元组中找出4的下标位置，没有报错：ValueError: tuple.index(x): x not in tuple

# 拆包

t1 = (4, 7, 3)

# a,b =t1   # ValueError: too many values to unpack(拆包) (expected（希望，盼望） 2)
# x,y,z=(6,) #ValueError: not enough values to unpack (expected 3, got 1)

a, b, c = t1

print(a, b, c)

a = t1

print(a)

# 变量个数与元组个数不一致
t1 = (2, 5, 8, 9, 7)

a, *_, c = t1
print(a, c, _)

a, c, *_ = t1
print(a, c, _)

a, b, *c = t1
print(a, b, c)

t1 = (9, 4, 8, 6)

a, *b = t1
print(a, b)  # *b 表示未知个数0~n， 0-- []   多个元素的话 ~ [1,2,3,4,...]

print(*b)
'''
  字符串  x,y,*z = 'hello'  ---> x='h'  y='e'  z=['l','l','o']
  列表  x,y,*z =['aa',6,'hello','good','happy','lucky']  ---> x='aa'  y=6  z=['hello','good','happy','lucky']

'''

'''
 t1=(9,4,8,6)

'''

t1 = (9,)

x, *y = t1

print(x, y)  # 9,[]

# 添加元素
y.append('a')
y.append('b')
print(y)  # ['a','b']

print(*y)  # print()   print(4,8,6)  4 8 6

'''
元组：
1. 符号:(1,2,3)  tuple
2. 关键字:tuple
3. 元组的元素只能获取，不能增删改

符号:
+
*
is  not
in  not in 

系统函数：
max()
min()
sum()
len()
sorted()   ----> 排序，返回的结果就是列表
tuple()  ---->元组类型的强制转换

元组自带函数:
index() 
count()


拆装包:
x,*y =(1,2,3,4,5)
print(y)
print(*y)

'''

t2 = (4, 5) + (1, 2)

print(t2)

t3 = (3, 4) * 2

print(t3)

print(t2 is t3)

print(3 not in t3)

print(len(t2))

print(tuple(sorted(t2)))
