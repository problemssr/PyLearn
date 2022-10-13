# 继承: is a , has a
'''
公路(Road)：
		属性：公路名称，公路长度

车(Car)：
    属性：车名，时速
    方法：1.求车名在那条公路上以多少的时速行驶了多长，
             get_time(self,road)
          2. 初始化车属性信息__init__方法
           3. 打印对象显示车的属性信息

'''
import random


# 声明（定义）Road
class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


# 声明(定义)Car
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # road = r   road 与 r指向同一个地址空间
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度:{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京藏高速', 12000)  # name  len
print(r.name)
r.name = '京哈高速'

audi = Car('奥迪', 120)

print(audi)

audi.get_time(r)  # 对象

#

# student  book   computer
'''
 知识点：
 1. has  a
    一个类中使用了另外一种自定义的类型

    student使用computer  book
2. 类型：
    系统类型：
       str  int  float
       list  dict  tuple  set
    自定义类型：
        算是自定义的类，都可以将其当成一种类型
        s = Student()
        s是Student类型的对象

'''


class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网....')

    def __str__(self):
        return self.brand + '---' + self.type + "---" + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '----' + str(self.number)


class Student:  # has a
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过此书！')
                break
        else:
            # 将参数book添加到列表中
            self.books.append(book)
            print('添加成功！')

    def show_book(self):
        for book in self.books:  # book就是一个book对象
            print(book.bname)

    def __str__(self):
        return self.name + "---" + str(self.computer) + '--------' + str(self.books)


# 创建对象
computer = Computer('mac', 'mac pro 2018', '深灰色')

book = Book('盗墓笔记', '南派三叔', 10)

stu = Student('songsong', computer, book)
print(stu)

# 看借了哪些书
stu.show_book()

book1 = Book('鬼吹灯', '天下霸唱', 8)

stu.borrow_book(book1)

print('---------------------')

stu.show_book()

list1 = [12, 'abc', [1, 2, 3], book, computer]


# is a   base class   父类  基类
# Exception
'''
继承：
  Student，Employee，Doctor  ---》 都属于人类
  相同代码 ---》 代码冗余，可读性不高

  将相同代码提取----》Person类
    Student，Employee，Doctor  ---》 继承Person

    class Student(Person):
        pass
 特点:
   1. 如果类中不定义__init__，调用父类 super class的__init__
   2. 如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
   3. 如何调用父类__init__:
       super().__init__(参数)
       super(类名,对象).__init__(参数)
    4. 如果父类有eat(),子类也定义一个eat方法，默认搜索的原则：先找当前类，再去找父类
       s.eat()
       override： 重写（覆盖）
       父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    5.子类的方法中也可以调用父类方法：
       super().方法名(参数)

'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print('{}正在学习{}课程'.format(self.name, course))

    def eat(self, food):
        super().eat()
        print(self.name + "正在吃饭...,喜欢吃：" + food)


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('阿文', 18, 'python1905')
s.run()
s.study('python基础')
s.eat('满汉全席')

e = Employee('tom', 23, 10000, 'king')
e.run()

lists = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
d = Doctor('lucy', 30, lists)
d.run()

'''
编写一个简单的工资管理程序,系统可以管理以下四类人：工人（worker）、销售员(salesman)、经理(manager)、销售经理（salemanger）。
所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
  1）工人：工人具有工作小时数和时薪的属性，工资计算法方法为工作小时数*时薪。
  2）销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例。
  3）经理：具有固定月薪的属性，工资计算方法为固定月薪。
  4)销售经理：工资计算方法为销售额*提成比例+固定月薪。
请根据以上要求设计合理的类，完成以下功能：
   1）添加所有类型的人员
   2）计算月薪
   3）显示所有人工资情况
'''


class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = '工号:{},姓名:{},本月工资:{}'.format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        money = self.hours * self.per_hour
        self.salary += money
        return self.salary


class Salesman(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percent = percent

    def getSalary(self):
        money = self.salemoney * self.percent
        self.salary += money
        return self.salary


# 创建子类对象
w = Worker('001', 'king', 2000, 160, 50)
s = w.getSalary()
print('月薪是:', s)
print(w)
print('----------------------------------------')
saler = Salesman('002', 'lucy', 5000, 50000000, 0.003)
s = saler.getSalary()
print('月薪是:', s)
print(saler)
