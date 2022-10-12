# 列表推导式  字典推导式  集合推导式
# 旧的列表 ----》新的列表

# 1. 列表推导式:  格式: [表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]

#  过滤掉长度小于或者等于3的人名
names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob', 'ha']
result = [name for name in names if len(name) > 3]
print(result)

result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 将1-100之间能被3整除，组成一个新的列表

newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)

# 0~5 偶数  0~10奇数
# [(偶数，奇数),(),(),()]  [(0,1),（0,3）,(0,5),(0,7),(0,9),(2,1),(2,3),...]

newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]

print(newlist)

# list1 =[[1,2,3],[4,5,6],[7,8,9],[1,3,5]]  --->[3,6,9,5]
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist = [i[-1] for i in list1]

dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}

list1 = [dict1, dict2, dict3, dict4]  # [{},{},{},{}]

# if薪资大于5000加200，低于等于5000加500

newlist = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list1]
print(newlist)

a = map(lambda employee: employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500, list1)
print('---->', list(a))

newlist = [{'name': person['name'], 'salary': person['salary'] + 200} if person['salary'] > 5000
           else {'name': person['name'], 'salary': person['salary'] + 500}
           for person in list1]
'''
def func(names):
    newlist=[]
    for name in names:
        if len(name)>3:
            name = name.title()
            newlist.append(name)
    return newlist


def func():
    newlist=[]

    for i in range(5):  # 偶数
        if i%2==0:
            for j in range(10):
                if j%2!=0:
                    newlist.append((i,j))

    return newlist


'''

# def func():
#     newlist = []
#
#     for i in range(5):  # 偶数
#         if i % 2 == 0:
#             for j in range(10):
#                 if j % 2 != 0:
#                     newlist.append((i, j))
#
#     return newlist
#
#
# x = func()
# print(x)


# 集合推导式  {}类似列表推导式，在列表推导式的基础上添加了一个去除重复项

list1 = [1, 2, 1, 3, 5, 2, 1, 8, 9, 8, 9, 7]

set1 = {x - 1 for x in list1 if x > 5}

print(set1)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}

newdict = {value: key for key, value in dict1.items()}

print(newdict)

# 可迭代的对象：1. 生成器  2. 元组 列表 集合 字典 字符串
# 如何判断一个对象是否是可迭代？
from collections import Iterable

list1 = [1, 4, 7, 8, 8]
f = isinstance(list1, Iterable)
print(f)

f = isinstance('abc', Iterable)
print(f)

f = isinstance(100, Iterable)
print(f)

g = (x + 1 for x in range(10))
f = isinstance(g, Iterable)
print(f)

'''
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
特点:
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退。
[1,2,3,5,6]

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可迭代的 是不是肯定就是  迭代器？
生成器是可迭代的，也是迭代器
list是可迭代的，但不是迭代器

list----> iter(list)  ---> 迭代器 next()

'''

list1 = [1, 2, 3, 4, 5]
list1 = iter(list1)  # 通过iter()函数将可迭代的变成了一个迭代器

print(next(list1))
print(next(list1))


