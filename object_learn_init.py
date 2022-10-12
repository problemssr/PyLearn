# 函数 和  类里面定义的：方法
#
# def func(name):
#     print('---->', name)
#
#
# username = 'admin'
# func(username)

def func(names):
    for name in names:
        print(name)


name_list = ['aa', 'bb', 'cc']
func(name_list)


class Phone:
    # 魔术方法之一: 称作魔术方法 __名字__()
    def __init__(self):  # init 初始的，初始化
        self.brand = 'xiaomi'
        self.price = 4999

    def call(self):  # self是不断发生改变
        print('-------->call')
        print('价格:', self.price)  # 不能保证每个self中都存在price


p = Phone()
p.call()

p1 = Phone()
p1.price = 5999
p1.call()

# p.price = 1000
# p.call()  # p.call()   p对象
#
# p1 = Phone()
# p1.call()

# print(Phone.price)
