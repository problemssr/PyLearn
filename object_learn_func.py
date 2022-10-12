# 类中方法：动作
# 种类: 普通方法  类方法  静态方法  魔术方法

'''
普通方法格式:
def 方法名(self[,参数，参数])：
    pass

'''


class Phone:
    brand = 'xiaomi'
    price = 4999
    type = 'mate 80'

    # Phone类里面方法：call
    def call(self):
        print('self----------->', self)
        print('正在访问通讯录:')
        for person in self.address_book: # [{},{}]
            print(person.items())
        print('正在打电话.....')
        print('留言:', self.note)


phone1 = Phone()
phone1.note = '我是phone1的note'
phone1.address_book = [{"159008867454": "于鹏"}, {"159008860000": "晓伟"}]
print(phone1, '-------1---')
phone1.call()  # call(phone1)  ---> self.note

print('*' * 30)
phone2 = Phone()
phone2.note = '我是phone22222222的note'
print(phone2, '-------2---')
phone2.call()  # call(phone2) ---> self.note
# phone2.note


class Person:
    name = '张三'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}正在吃{}！。。。'.format(self.name, food))

    def run(self):
        print('{},今年{}岁，正在跑步'.format(self.name, self.age))


p = Person('李四', 20)
p.name = 'lisi'
p.eat('红烧肉')
p.run()

p1 = Person('wangwu', 22)
p1.name = '王五'
p1.eat('狮子头')
p1.run()

p2 = Person('zhaoliu', 17)
p2.run()


# eat()