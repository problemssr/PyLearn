# 类方法
'''
 特点:
  1. 定义需要依赖装饰器@classmethod
  2. 类方法中参数不是一个对象，而是类
     print(cls)  # <class '__main__.Dog'>
  3. 类方法中只可以使用类属性
  4. 类方法中可否使用普通方法？  不能

类方法作用:
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作(功能)

'''


class Dog:

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self   对象
        print('{}在院子里跑来跑去!'.format(self.nickname))

    def eat(self):
        print('吃饭。。。。。')
        self.run()  # 类中方法的调用，需要通过self.方法名()

    @classmethod
    def test(cls):  # cls  class
        print('----------')
        print(cls)  # <class '__main__.Dog'>
        # self.run()
        # print(cls.nickname)   报错
        # print(self.nickname)


Dog.test()

# d = Dog('大黄')
#
# d.run()  # 调用run
#
# d.test()
