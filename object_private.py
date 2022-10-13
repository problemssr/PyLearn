# 私有化: 如果想让类的内部属性不被外界直接访问，可以在这个属性的前面加两个下划线__ ,在Python中，如果一个属性的前面出现 __,就表示这个属性只能在当前类的方法中被直接访问，不能通过对象直接访问，这个变量就被称为私有变量
# 封装: 1. 私有化属性  2.定义公有set和get方法
# __属性： 就是将属性私有化，访问范围仅仅限于类中
'''
好处：
1. 隐藏属性不被外界随意修改
2. 也可以修改：通过函数
   def setXXX(self,xxx):
       3. 筛选赋值的内容
         if xxx是否符合条件
             赋值
          else:
             不赋值
3.如果想获取具体的某一个属性
  使用get函数
    def getXXX(self):
       return self.__xxx
'''


class Student:
    # __age = 18  # 类属性

    def __init__(self, name, age):
        self.__name = name  # 长度必须6位
        self.__age = age
        self.__score = 59

    # 定义公有set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('年龄不在规定的范围内')

    # get是为了取值
    def getAge(self):
        return self.__age

    # 修改名字的时候，长度必须6位
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字不是六位')

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{},年龄:{},考试分数:{}'.format(self.__name, self.__age, self.__score)


yupeng = Student('yupeng', 18)
print(yupeng)
yupeng.setAge(120)
print(yupeng)
# yupeng.name = 'xiaopeng'
yupeng.setName('xiaopeng')
print(yupeng)

# 就想拿到于鹏年龄
print(yupeng.getAge())

feifei = Student('feifei', 20)
print(feifei)

# yupeng.age = 21
# print(yupeng.__score)
# yupeng.__score = 95
# print(yupeng)
print(dir(Student))
print(dir(feifei))


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字必须6位')

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{},年龄:{}'.format(self.__name, self.__age)

    # attribute: setName  getName  __str__  __init__


s = Student('yupeng', 18)

print(s)

print(dir(Student))

print(dir(s))
# print(s.__name)  # _Student__name
print(s._Student__age)  # 其实它就是__age ,只不过系统自动改名字了。
print(s.__dir__())
print(__name__)


# 在开发中看到一些私有化处理： 装饰器
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 先有getxxx，
    @property
    def age(self):
        return self.__age

    # 再有set，因为set依赖get
    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print('不在规定的范围内')

    # def setAge(self, age):
    #     if age > 0 and age < 100:
    #         self.__age = age
    #     else:
    #         print('不在规定的范围内')
    #
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名:{},年龄:{}'.format(self.name, self.__age)


s = Student('peng', 20)
#
s.name = 'xiaopeng'
print(s.name)

s.age = 130
print(s.age)
print(s.__dir__())
print(dir(s))

# 私有化赋值
# s.setAge(30)
# print(s.getAge())
