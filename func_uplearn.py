# 内部函数
'''
特点:
1. 可以访问外部函数的变量
2. 内部函数可以修改外部函数的可变类型的变量比如：list1
3. 内部函数修改全局的不可变变量时，需要在内部函数声明global 变量名
   内部函数修改外部函数的不可变的变量时，需要在内部函数中声明: nonlocal 变量名
4. locals() 查看本地变量有哪些，以字典的形式输出
   globals() 查看全局变量有哪些，以字典的形式输出（注意里面会有一些系统的键值对）


'''


def func():
    # 声明变量
    n = 100  # 局部变量
    list1 = [3, 6, 9, 4]  # 局部变量

    # 声明内部函数
    def inner_func():
        nonlocal n
        # 对list1里面的元素进行加5操作
        for index, i in enumerate(list1):
            # 0  3
            list1[index] = i + n

        list1.sort()

        # 修改n变量
        n += 101

    # 调用一下内部的函数
    inner_func()

    print('打印老大n:',n)

    print('打印老二list1:',list1)


# 调用func
func()

a = 100  # 全局变量
print(globals())

# 定义函数
def func():
    # 声明变量
    b = 99
    # 声明函数
    def inner_func():
        global a
        nonlocal b
        c = 88
        # 尝试修改
        c += 12
        b += 1
        a += 10
        # 尝试打印
        print(a, b, c)
    # 调用内部函数
    inner_func()
    # 使用locals()内置函数进行查看。可以看到在当前函数中声明的内容有哪些
    # locals()是一个字典。key：value
    print(locals())


# 调用函数
func()

# 闭包
# 在函数中提出的概念，
'''
条件：
1. 外部函数中定义了内部函数
2. 外部函数是有返回值
3. 返回的值是：内部函数名
4. 内部函数引用了外部函数的变量

格式:
def 外部函数():
    ...
    def 内部函数():
        ....
    return 内部函数


'''

def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    print(locals())

    return inner_func


# print(a)
# inner_func()


x = func()

print(x)  # <function func.<locals>.inner_func at 0x00000000021500D0>

# x就是内部函数，x()就表示调用函数
x()

# 闭包

def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('相加之后的结果是:', s)

    return inner_func


# 调用func
ifunc = func(6, 9)  # ifunc就是inner_func   ifunc = inner_func

# 调用返出来的内部函数
ifunc()

# 闭包的应用
# 闭包：
'''
1. 保存返回返回闭包时的状态（外层函数变量）


'''


# 闭包
#
# def func(a, b):
#     c = 10
#
#     def inner_func():
#         s = a + b + c
#         print('相加之后的结果是:', s)
#
#     return inner_func
#
#
# # 调用func
# ifunc = func(6, 9)  # ifunc就是inner_func   ifunc = inner_func
# ifunc1 = func(2, 8)
# ifunc2 = func(1, 9)
#
# print(ifunc)
# print(ifunc1)
# print(ifunc2)
#
# ifunc1()
# ifunc()
# ifunc2()


# 计数器
def generate_count():
    container = [0]

    def add_one():

        container[0] = container[0] + 1  # [2]
        print('当前是第{}次访问'.format(container[0]))

    return add_one


# 内部函数就是一个计数器
counter = generate_count()   # counter = add_one

counter()  # 第一次的访问
counter()  # ....
counter()


'''

在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
并且把里面的函数返回，我们把这种情况叫闭包

内部函数对外部函数作用域里变量的引用
内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。


访问外部函数的可变类型局部变量可不加nonlocal
访问外部函数的不可变类型局部变量要加 nonlocal


闭包有什么缺点呢？
闭包的缺点1，作用域没有那么直观
闭包的缺点2，因为变量不会被垃圾回收所以有一定的内存占用问题。

闭包作用：1.可以使用同级的作用域
闭包作用：2.读取其他元素的内部变量
闭包作用：3.延长作用域


闭包总结
1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成.
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存.
3.闭包的好处，使代码变得简洁，便于阅读代码。
4.闭包是理解装饰器的基础

'''

def func():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print(s)

    def inner_func2():   # define
        inner_func1()  # 调用inner_func1
        print('-----------> inner_func2',a)
        return 'hello'

    return inner_func2   # 0x0000000001DE0158


# 调用func
f = func()
print(f)
ff = f()  # inner_fun2()
print(ff)

# 装饰器
'''
 加入购物车，付款，修改收货地址，。。。
 判断用户的登录状态

'''


def func(number):
    a = 100

    def inner_func():
        nonlocal a
        nonlocal number
        number += 1

        for i in range(number):
            a += 1
        print('修改后的a:', a)

    return inner_func


# 调用func
f = func(5)
f()

# 函数作为参数
a = 50
f1 = func(a)  # a是一个实参
print(f1)

# 地址引用
a = 10  # 声明整型变量
b = a


def test():  # 声明函数
    print('------test-------')


# t = test
# test()
# t()

# def func(f):  # f=test
#     print(f)  # <function test at 0x0000000001D01E18>
#     f()  # -------test---------
#     print('------------>func')
#
#
# # 调用
# func(test)

'''
特点:
1. 函数A是作为参数出现的（函数B就接收函数A作为参数）
2. 要有闭包的特点
'''


# 定义一个装饰器
def decorate(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('--------->刷漆')
        print('--------->铺地板', a)
        print('--------->装门')

    print('wrapper加载完成......')
    return wrapper


# 使用装饰器
@decorate
def house():
    print('我是毛坯房....')

'''
默认执行的:
1. house被装饰函数，
2. 将被装饰函数作为参数传给装饰器decorate
3. 执行decorate函数
4. 将返回值又赋值给house

'''
print(house)
house()
# def house1():
#     house()
#     print('刷漆')
#     print('铺地板')


# 调用函数house
# house()

# 匿名函数: 简化函数定义
# 格式:  lambda  参数1, 参数2.. : 运算

# def func():
#     print('aaaa')
#
#
def add(a, b):
    s = a + b
    return s


f = add

s = lambda a, b: a + b

print(s)  # s 就是函数function

result = s(1, 2)

print(result)

s1 = lambda x, y: x * y

result = s1(2, 5)

print(result)


# 匿名函数作为参数
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)


# 调用func
func(1, 2, lambda a, b: a + b)

# 匿名函数与内置函数的结合使用:
# max  sorted   zip ...

list1 = [3, 5, 8, 9, 0]
m = max(list1)

print('列表的最大值:', m)

list2 = [{'a': 10, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 29, 'b': 20}]

m = max(list2, key=lambda x: x['a'])
print('列表的最大值:', m)

'''
 students =[
 {'name':'tom','age':20},
 {'name':'lucy','age':19},
 {'name':'lily','age':13},
 {'name':'mark','age':21},
 {'name':'jack','age':23},
 {'name':'steven','age':18},
 ]

'''

# 递归函数: 函数自己调用自己
'''
普通：def func（）：pass
匿名函数: lambda 参数: 返回结果
递归函数: 普通函数的一种表现形式

特点:
1. 递归函数必须要设定终点
2. 通常都会有一个入口
'''


def sum(n):  # 1~n
    '''
    求和的函数
    :param n: 从1~n累加和
    :return: 求和的结果
    '''
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


result = sum(10)
#
# print(result)

# def sum1(n):
#     if n==100:
#         pass
#     else:
#         pass



# s = 0
# for i in range(11):
#     s += i
# print(s)


def f1(n):
    if n>0:
        print('---->',n)
        f1(n - 1)
    else:
        print('----->',n)


f1(10)

# map

list1 = [3, 4, 6, 7, 8, 9, 9, 0, 2, 5]

result = map(lambda x: x + 2, list1)
print(list(result))

# for index,i in enumerate(list1):
#     list1[index]=i+2

func = lambda x: x if x % 2 == 0 else x + 1

result = func(5)
print(result)

# 对列表中的奇数进行加1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))

# for index, i in enumerate(list1):
#     if i % 2 != 0:
#         list1[index] = i + 1
#
# print(list1)


# reduce(): 对列表中的元素进行加减乘除运算的函数
from functools import reduce

tuple1 = (3, 5, 7, 8, 9, 1)

result = reduce(lambda x, y: x + y, tuple1)

print(result)

tuple2 = (1,2,3)

result = reduce(lambda x, y: x - y, tuple2, 10)
print(result)

# 动手测试减法
list1 = [12, 6, 8, 98, 34, 36, 2, 8, 0]

result = filter(lambda x: x > 10, list1)

print(list(result))

print(list1)

# def func(list1):
#     list2 = []
#     for i in list1:
#         if i > 10:
#             list2.append(i)
#     return list2


students = [
    {'name': 'tom', 'age': 20},
    {'name': 'lucy', 'age': 19},
    {'name': 'lily', 'age': 13},
    {'name': 'mark', 'age': 21},
    {'name': 'jack', 'age': 23},
    {'name': 'steven', 'age': 18},
]

# 找出所有年龄大于20岁学生

result = filter(lambda x: x['age'] > 20,students)
print(list(result))


# 按照年龄从小到大排序

students = sorted(students,key=lambda x:x['age'],reverse=True)

print(students)

'''
max()  
min()
sorted()

map(): 
reduce()
filter()  


'''

# 递归
# 入口 1   出口  10

def sum(n):
    if n == 10:
        return 10
    else:
        return n + sum(n + 1)


result = sum(1)

print(result)





