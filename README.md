# Python 基础

## 1.初识python

## 2.字符串

```python
总结：
大小写： lower()
upper()
查找: find()
rfind()
替换: replace()
分割: split()
连接: join()
编码： encode()
decode()
的使用
个数： count()
去除空格：  strip()
lstrip()
rstrip()
用于判断的:
startswith()
开头判断
endswith()
结尾判断
isalpha()
字母判断
isdigit()
数字判断
```

## 3.列表，字典，元组，集合

```markdown
回顾:
数据类型:
字符串： 声明:
''
""
''' '''

符号:

+

*

in not in is not is
[]

获取字符串元素:

s = 'hello' s[0] ~ s[len(s)-1]

切片:
s[start:end[:step]]  包前不包后

内置函数:
lower()  upper()
replace()
split()  
find()  rfind()  lfind()
strip()  lstrip()  rstrip()
join()
isalpha()  isdigit()
...

‘容器’:

列表: list 特点:  保存多个元素，元素有顺序。可以通过下标找到对应的元素。  
可以增加，删除，修改元素，查询 内置函数:
append extend insert remove pop clear , del sort reverse index count

元组: tuple 特点: 保存多个元素。 不可以增加，删除，修改元素。但是可以查询元素

内置函数: index count 支持下标操作： t= （1,2,3） t[0],t[1:]

字典: dict 特点: 键值对保存元素。 键是唯一的，而值不唯一。 可以支持对键值对的增删改查 内置函数:
增加(修改)键值对:  dict1={} dict1[key]=value  
删除键值对: dict1.pop()   dict1.popitem()   dict1.clear()
查询: items()  values()  keys()

集合: set 关键字 无序的不重复的元素 作用: 不重复特点

```

## 3.可变元素和不可变元素，函数

```markdown
集合： list tuple ---》set()
无序不重复的序列，集合 无序 ---》 跟下标相关

s ={1,2,3,4,5} ---->s[1]

for i in s:
print(i)

内置函数： 添加： add update 删除: remove discard pop clear

运算相关函数：

- difference()
  | union()
  & intersection()
  ^ symmetric_difference()

可变和不可变： 可变: 地址不变里面内容改变 list dict set 不可变: 只要内容改变，必须改变地址 int str float tuple frozenset

类型转换:
str ---> list set ... 相互的转换

list ---> set tuple dict 相互的转换

函数:

增加代码的复用性，减少了代码冗余

def 函数名([参数,...]):
函数体（重复性代码）

没有参数:

def add():
result = 1+3 print(result)

调用:
add()   ---> 4

有参数:

def add(a,b):
result = a+b print(result)

调用:
add(1,3)
add(5,6)
add(100,29)

总结:

1.参数的种类： 2.返回值return 3.函数间相互调用 4.局部和全局变量

```

## 4.函数进阶

```python
作用域：LEGB

L: local
本地
局部变量

E: encloseing
嵌套

G: Global
全局

B: built - in 内置的

嵌套函数：

闭包：
1.
内层函数
2.
内层函数引用外层函数的变量
3.
返出内层函数

装饰器:
1.
内层函数
2.
内层函数引用外层函数的变量
3.
返出内层函数
4.
函数作为外层函数参数

使用装饰器:


@装饰器名字
def 函数名():
    pass


# 总结函数：
普通函数:


def 函数名([参数, ...]):
    函数体


1.
如何定义函数
2.
调用函数

参数：
1.
无参数：

def func():
    pass


func()

2.
有参数:
一般参数:


def func(a, b):
    pass


func(1, 2)

可变参数:


def func(*args, **kwargs):  args单个元素


kwargs
关键字参数
pass

func()

func(1)

func(a=10)

默认值:


def func(a=10, b=10):
    pass


func()

func(100)

关键字参数:

func(b=99)

返回值:
return

没有返回值


def func():
    print('-----')


x = func() - --->x = None

有返回值:


def func():
    return 'a'


x = func() - ----> x = 'a'


def func():
    return 'a', 'b'


x = func() - ----> x = ('a', 'b')

嵌套函数 - --》 闭包 - --》 装饰器


def func():
    def wrapper():
        ....

    return wrapper


变量的作用域： LEGB
global
nonlocal
globals()
locals()
LEGB

L: local
本地
局部变量
E: encloseing
嵌套
G: Global
全局
B: built - in 内置的

装饰器:

单层装饰器


def decorate(func):
    def wrapper(*args, **kwargs):
        ....

    return wrapper


@decorate
def house():
    pass


@decorate
def f1(a, b):
    pass


多层装饰器:


@zhuang2
@zhuang1
def f1(a, b):
    pass


装饰器带参数:


def outter(a):
    def decorate(func):
        def wrapper(*args, **kwargs):
            ....

        return wrapper


return decorate


@zhuang(10)
def house():
    pass


@zhuang(100)

:

def street():
    pass


匿名函数: lambda 参数：返回值

递归函数： 自己调用自己。


```

# 5.文件

```python
文件操作：

open(path,mode)

mode ----> r
s.read()
s.readline()
s.readlines()
s.readable()

with open('a1.txt') as fstream:
    pass

FileNotFoundError: [Errno 2] No such file or directory: 'a1.txt'

mode ---->w,a

with open('a1.txt', 'w') as wstream:   ----> 如果指定的文件不存在，则自动创建。
    wstream.write('hello')

write()
writelines()
writeable()


os模块：
os.path

absolute 绝对的  c:\p1\girl.jpg

C:\Users\running\Desktop\python基础\day13(6-14)\代码\day13_文件\images\girl.jpg


文件：
文件操作：
  open()
  path,filename:
    path:
      绝对路径：C:\Users\running\Desktop\python基础\day13(6-14)\代码\day13_文件\images\girl.jpg
      相对路径：相对当前文件的路径。返回上层目录： ../
  mode:
  读:  rb  r
  写:  wb  w

  stream  =  open(file,mode)
  stream.read()
  stream.write()
  stream.close()

  with open(file,mode) as stream:
        操作代码


  os模块：

  os.path:常用函数
    os.path: 常用函数
     dirname() 获取指定文件的目录
     join()    拼接获取新的路径
     split()   分割(文件目录，文件名)
     splittext()  分割(文件目录\文件名,文件的扩展名)
     getsize()   获取文件大小

     isabs()   判断是否是绝对路径
     isfile()  判断是否是文件
     isdir()   判断是否是文件夹


  os常用函数
    os模块下方法:
    os.getcwd()  获取当前目录
    os.listdir()  浏览文件夹
    os.mkdir()  创建文件夹
    os.rmdir()  删除空的文件夹
    os.remove()  删除文件
    os.chdir()  切换目录

```

# 6.异常

```python
异常：
语法错误
异常

系统抛出异常

list1=[]
list1.pop()

处理异常:

try:
   可能发生异常代码
except:
   有异常才会进入代码
[except 异常类型 as err:
     ...
]
[
 else:
   没有异常才会进入代码
]
[
finally:
   无论有没有异常都会执行的代码
]


抛出异常： 手动异常 raise
 格式:
     raise 异常类型('提示信息')

```

# 7.生成器

```python
生成器:generator
 
 定义生成器方式:
 
 1. 通过列表推导式方式
    g = (x+1 for x in range(6)) 
    
 2. 函数+yield
    def func（）:
        ...
        yield 
    
    g= func()   

 产生元素：
   1.next(generator)  ---> 每次调用都会产生一个新的元素，如果元素产生完毕，再次调用的话就会产生异常
   2.生成器自己的方法：
       g.__next__()
       g.send(value)  
 
  应用: 协程
```

# 8.列表推导式  字典推导式  集合推导式 可迭代与生成器

```python
列表推导式:  格式: [表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]

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
    
生成器与迭代器关系：

可迭代的：isinstance(x,Iterable)  ---> True
可迭代的可以变成迭代器，但是需要iter()进行转换

列表推导式：
[表达式 for 变量 in 列表]

[x+2 for x in list1]---->新的列表

1. [表达式 for 变量 in 列表 if 条件]
    [x+2 for x in list1 if x%2==0]

2. [结果A if 条件 else 结果B for x in list1]

  [x+2 if x%2==0 else x+1 for x in list1 ]

集合推导式： {表达式 for 变量 in 列表} ---> 类似列表推导式，但是没有重复元素
字典推导式：{key,value  for k,v in 字典.items()}


生成器:generator
1. 使用类似的列表推导式  g = (表达式 for 变量 in 列表)
    此时的g就是生成器
2. 函数+yield

   def func():
       ....
       yield
       ....

   g = func()

得到里面的元素:

    系统函数： next(g)

    生成器里面函数:  __next__() , [send(None),send(e)]


可迭代的与迭代器：
1.生成器  2. 字符串,列表,集合,...

Iterable

isinstance(x,Iterable)  --->True,False


生成器就是一个迭代器  ----》 next(g) --->下一个元素
next(list) ---> iter(list)  ---->next(iter(list))  ----> 下一个元素


面向对象
类

class 类名:
    特征： 属性
    动作:  方法


实例,对象

huawei = Phone()
huawei.price = 5999
```

# 9.面向对象类的方法

```python
类中的方法:
普通方法
def func(self):   ----> self对象
    pass
类方法
@classmethod
def func(cls):  ---》cls  类
    pass
静态方法
@staticmethod
def func():
    pass
魔术方法
__init__ , __str__

__new__   __call__   __del__

n=5
n1 = n

p = Person()
p1 = p

del p1
del p
ref = 0  ---->__del__
```

# 10.面向对象私有化，封装，继承，多态

```python
封装：
私有化属性，定义公有的set和get方法
 私有化：
    __age
    def __show(self):
        pass

    ---> _类名_属性

  私有化： 封装  将属性私有化，定义公有set和get方法
  def setAge(self,age):
      判断
  def getAge(self):
     return self.__age

  s.setAge(20)
  s.getAge()

  class Student:
      def __init__(self,age):
            self.__age=age

      @property
      def age(self):
        return ...

      @age.setter
      def age(self,age):
        self.__age=age

  s= Student()
  s.age=10
  print(s.age)


 继承：
   has a
   class Student:
     def __init__(self,name,book):
        pass

   is a
    父类   子类
    class Person:
        def run(self):
            ....

    class Student(Person):
        ....

        def study(self):
            ....

        def run(self):
            super().run()
            .....

    s= Student()
    s.study()
    s.run()


    1. __init__
    2. 重写方法

  多继承：（了解）
    class A:
        pass
    class B:
        pass
    class C(A,B):
        pass
    现在执行环境python3

    新式类: 广度优先

    D.__mro__  --->查看搜索顺序
    import inspect
    print(inspect.getmro(D))

继承：
is a:
  父类  子类
  class Student(Person):
    pass

has a:
  class Student:
       def __init__(self,book,computer):
           book 是自定义类型   ---  系统类型

  s = Student()

多继承：
class C(A,B):
    pass

C.__mro__

多态：

class Person:

   def feed_pet(self,pet):
    isinstance(pet,Pet):
        pass

```

# 11.单例模式，模块，包，系统路径
```python
单例：__new__
class Singleton：
    __instance=None

    def __new__(cls):
        判断instance是否是None
        if cls.__instance is None:
            return 。。。
        return cls.__instance
扩展： 元类   。。

模块：
自定义：
 xxx.py

 import xxx

 from xxx import xx

 from xxx  import *   + __all__ =[]

 __name__ ---> 自己:__main__  别的使用: 模块名


 包：
   user
     |-- __init__.py   只要包的导入，都会默认执行__init__.py文件  __all__ = [  ] + from 包名 import *
     |-- xxx.py
     |-- xx.py
          |-- add
    article
        |-- aa.py

     bb.py

     from user.xx import add
     add()

  循环导入：避免
  1. 重构代码
  2. 将导入语句放到函数中
  3. 把导入语句放到模块最后

系统：

   sys:  sys.path   sys.version  sys.argv
```