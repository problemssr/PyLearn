#   封装  继承  多态 ----》 面向对象
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可以接收cat，也可以接收dog，还可以接收tiger
        # isinstance(obj,类)  ---》 判断obj是不是类的对象或者判断obj是不是该类子类的对象
        if isinstance(pet, Pet):
            print('{}喜欢养宠物:{}，昵称是:{}'.format(self.name, pet.role, pet.nickname))
        else:
            print('不是宠物类型的。。。。')


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('昵称:{},年龄:{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠....')


class Dog(Pet):
    role = '狗'

    def watch_house(self):
        print('看家高手....')


class Tiger:
    def eat(self):
        print('太可怕了，可以吃人...')


# 创建对象
cat = Cat('花花', 2)

dog = Dog('大黄', 4)

tiger = Tiger()

person = Person('家伟')

person.feed_pet(cat)
person.feed_pet(dog)
print('----------------------------')
person = Person('pengpeng')

person.feed_pet(tiger)

# Pet
#  pet  父类      cat   dog 子类
#  pet  大类型    cat  dog 小类型
