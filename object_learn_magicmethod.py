# 魔术方法
# __init__:初始化魔术方法
# 触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）

# __new__: 实例化的魔术方法
# 触发时机： 在实例化对时触发

# __call__: 对象调用方法
# 触发时机: 将对象当成函数使用的时候，会默认调用此函数中内容

# __del__:  delete的缩写 析构魔术方法
# 触发时机：当对象没有用（没有任何变量引用）的时候被触发



class Person:

    def __new__(cls, *args, **kwargs):  # __new__  向内存要空间 ---》 地址
        print('--------->new')
        position = object.__new__(cls)  # 0x637843784
        print(position)  # <__main__.Person object at 0x000000000278B860>
        return position  # 地址

    def __init__(self, name):
        print('---------->init', self)  # <__main__.Person object at 0x000000000278B860>
        self.name = name

    def __call__(self, name):
        print('----------------->call')
        print('执行对象得到参数是：', name)


p = Person('aa')

print(p)  # <__main__.Person object at 0x000000000278B860>
print(p.name)
#
p('jack')

# def func():
#     pass
#
# func()

import sys

'''
__del__:
  1. 对象赋值
     p = Person()
     p1 =p
     说明： p和p1共同指向同一个地址

  2. 删除地址的引用
     del p1  删除p1对地址的引用

  3. 查看对地址的引用次数：
      import sys
      sys.getrefcount(p)

  4.  当一块空间没有了任何引用，默认执行__del__
       ref =0 

'''


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('------del---------')


p = Person('jack')
p1 = p
p2 = p
print(p1.name)
print(p2.name)

p1.name = 'tom'
print(p.name)
print(p2.name)

print(sys.getrefcount(p))  # 4

del p2
print('删除p2后打印:', p.name)

print(sys.getrefcount(p))  # 3

del p1
print('删除p1后打印:', p.name)

print(sys.getrefcount(p))  # 2

# del p
# print('删除p后打印:', p.name)   #


# 对象赋值
n = 5
n1 = n

print(n)

del n


#  __str__：
# 触发时机： 打印对象名 自动触发去调用__str__里面的内容
# 注意： 一定要在__str__方法中添加return，return后面内容就是打印对象看到内容

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名是:' + self.name + ',年龄:' + str(self.age)


p = Person('tom', 18)
print(p)

# 单纯打印对象名称，出来的是一个地址。地址对于开发者来书没有太大意义
# 如果想在打印对象名的时候能够给开发者更多一些信息量，

p1 = Person('jack', 20)
print(p1)

'''
总结：魔术方法
重点：
__init__ （构造方法，创建完空间之后调用的第一个方法）， __str__

了解:
__new__ 作用  开辟空间  

__del__ 作用  没有指针引用的时候会调用。99%都不需要重写

__call__  作用： 想不想将对象当成函数用。


大总结：
方法：
  普通方法  ---》 重点
      def 方法名(self,[参数]):
          方法体

      对象.方法()

      方法之间的调用：
      class A:
        def a(self):
            pass
        def b(self):
            # 调用a方法
            self.a()

  类方法: 
      @classmethod 
      def 方法名(cls,[参数]):
          pass

      类名.方法名()
      对象.方法名()

  静态方法: 
      @staticmethod
      def 方法名([参数]):
              pass

      类名.方法名()
      对象.方法名()

  魔术方法:
    自动执行方法

    print(p)  ---> __str__

'''
