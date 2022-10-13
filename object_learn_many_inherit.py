# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def eat(self):
#         print('------->eat1')
#
#     def eat(self,food):
#         print('------------>eat:',food)
#
# p = Person('jack')
# p.eat('狮子头')
class Base:
    def test(self):
        print('---------Base-----------')


class A(Base):
    def test(self):
        print('--->AAAAAAAAAA')


class B(Base):
    def test(self):
        print('----------->BBBBBBBB')


class C(Base):
    def test(self):
        print('----------->CCCCCCCCC')


class D(A, B, C):
    pass


d = D()
d.test()
import inspect

print(inspect.getmro(D))

print(D.__mro__)
# c.test1()
# c.test2()

'''
 python允许多继承，
 def 子类(父类1，父类2，..):
    pass

 如果父类中有相同名称方法，搜索顺序: 

'''

# 多继承的搜索顺序： 经典类  新式类
# class P1:
#     def foo(self):
#         print('p1--->foo')
#
#     def bar(self):
#         print('p1--->bar')
#
#
# class P2:
#     def foo(self):
#         print('p2--->foo')
#
#
# class C1(P1, P2):
#     pass
#
#
# class C2(P1, P2):
#     def bar(self):
#         print('C2---->bar')
#
#
# class D(C1, C2):
#     pass
#
#
# d = D()
#
# print(D.__mro__)
#
# d.foo()
# d.bar()

# 从左至右，深度优先

class P1(object):
    def foo(self):
        print('p1--->foo')

    def bar(self):
        print('p1--->bar')


class P2(object):
    def foo(self):
        print('p2--->foo')


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print('C2---->bar')


class D(C1, C2):
    pass


d = D()

print(D.__mro__)

d.foo()
d.bar()

# python 2