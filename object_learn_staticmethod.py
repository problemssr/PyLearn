# 补充类方法
'''
静态方法: 很类似类方法
1. 需要装饰器@staticmethod
2. 静态方法是无需传递参数（cls,self）
3. 也只能访问类的属性和方法，对象的是无法访问的
4. 加载时机同类方法

总结:
类方法  静态方法
不同：
  1. 装饰器不同
  2. 类方法是有参数的，静态方法没有参数

相同:
  1. 只能访问类的属性和方法，对象的是无法访问的
  2. 都可以通过类名调用访问
  3. 都可以在创建对象之前使用，因为是不依赖于对象

普通方法 与 两者区别:
不同:
   1. 没有装饰器
   2. 普通方法永远是要依赖对象，因为每个普通方法都有一个self
   3. 只有创建了对象才可以调用普通方法，否则无法调用。

'''


class Person:
    __age = 18

    def __init__(self, name):
        self.name = name

    def show(self):
        print('--------->', Person.age)

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('----------->类方法')

    @classmethod
    def show_age(cls):
        print('修改后的年龄是:', cls.__age)

    @staticmethod
    def test():
        print('---------->静态方法')
        # print(self.name)  语法错误
        print(Person.__age)


Person.update_age()
Person.show_age()
Person.test()


# print(Person.__age)

# p = Person()
# p.age = p.age+1  #
# p.show()