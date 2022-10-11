'''
使用函数的时候:
def aa(**kwargs):
    pass

aa(a=1, b='hello', c='tom')    --->将关键字装包成字典

'''


def aa(**kwargs):
    print(kwargs)


aa(a=1, b='hello', c='tom')  # 装包：{'a': 1, 'b': 'hello', 'c': 'tom'}

# 如果在开发的时候，已知一个字典

dict1 = {'a': 1, 'b': 'hello', 'c': 'tom'}

aa(**dict1)  # a=1, b='hello', c='tom'    拆包的过程


def bb(a, b, *c, **d):
    print(a, b, c, d)


bb(1, 2)  # 1 2 () {}

bb(1, 2, 3, 4)  # 1 2 (3,4) {}

bb(1, 2, x=100, y=200)  # 1 2 () {'x':100,'y':200}

bb(1, 2, 3, x=100)  # 1 2 (3,) {'x':100}

bb(1, 2, x=100, y=200, z=100)

'''
练习:
1.
def func(a,*args):
    print(a,args)

调用:
func(2,3,4,5)      2 (3,4,5)

func(2,[1,2,3,4])  2 ([1,2,3,4],)

func(2,3,[1,2,3,4,5])  2 (3,[1,2,3,4])

func(5,6,(4,5,7),9)  5 (6, (4, 5, 7), 9)

2.
def func(a,b=10,c=3,**kwargs):   关键字默认值
    print(a,b,c,kwargs)

func(1)  1 10  3  {}

func(2,b=10)  2 10  3 {}

func(3,5,7,a=1,b=2)  报错

func(3, c=5, b=7, x=1, y=2)  # 3 5 7 {'x': 1, 'y': 2}

3.
def func(a,*args,**kwargs):
    print(a,args,kwargs)

t=(1,2,3,4)
func(1,t)

l=[2,5,8]
func(1,l,a=9,b=6)

'''


# def func(a, *args):
#     print(a, args)
#
#
# func(2, [1, 2, 3, 4],5,'hello')
# func(5,6,(4,5,7),9)


# def func(a, b=10, c=3, **kwargs):
#     print(a, b, c, kwargs)
#
#
# func(1)  # 1 10 3 {}
#
# func(2, b=11)  # 2 11 3 {}
#
# func(3, c=5, b=7, x=1, y=2)  # 3 5 7 {'x': 1, 'y': 2}


def func(a, *args, **kwargs):
    print(a, args, kwargs)


t = (1, 2, 3, 4)
func(1, t)  # 1 ((1,2,3,4),)

l = [2, 5, 8]
func(1, l, c=9, b=6)  # 1 ([2, 5, 8],) {'c': 9, 'b': 6}

dict1 = {'1': 'a', '2': 'b', '3': 'c'}
func(1, *l, **dict1)
# func(1,2,5,8,1='a',2='b',3='c')
'''
courses = ['html','mysql','python']


'''


def func1(name, *args):
    if len(args) > 0:
        for i in args:  # ('html','mysql','python')
            print('{}学过了{}'.format(name, i))
    else:
        print('没有学任何编程知识！')


courses = ['html', 'mysql', 'python']

# 调用函数
func1('坤坤', *courses)  # 拆包

'''
无参数函数:

def func():
    pass

func()  ---->调用

有参数函数:
  1. 普通参数

  def func(name,age):
        pass

  func('aa',18)   ----> 形参与实参的个数要一致


  2. 可变参数:
   A. def func(*args):
          pass

      func()  ----> 函数调用时，实参的个数可以没有，也可以多个   *不能是关键字参数
      func(4)  func(5,'h')


  B. def  func(**kwargs):
         pass

     func(a=1,b=2)  ----> 函数调用时，实参的个数可以没有，也可以多个   **必须是关键字参数

  C. def func(*args,**kwargs):
         pass

    list1 = [1,3]
    dict1 = {'1':'a','2':'b'}
    func(*list1,**dict1)  # func(1,3,'1'='a','2'='b')

  D. 混用

  def func(name,*args,**kwargs):
        pass

  func('tom')   ----> 必须赋值

  3. 默认值+关键字

  def func(name,age=18):
        pass

  func('tom')  ----》 tom  18

  func('tom',age=20)   --->关键字赋值



'''

'''
 加入购物车
 判断用户是否登录，如果登录，成功加入购物车，否则提示请登录之后添

 成功 True   不成功  False

 def add_shoppingcart(goodsName):
    pass

 def login(username,password):
    pass

  调用
'''

islogin = False  # 用于判断用户是否登录变量  默认是没有登录的


def add_shoppingcart(goodsName):
    if islogin and goodsName:
        # 登录的
        print('成功将{}加入到购物车中！'.format(goodsName))
    else:
        # 没有登录
        print('用户没有登录或者没有添加任何商品！')


def login(username, password):
    if username == 'lijiaqi' and password == '123456':
        # 登录成功
        # print('登录成功')
        return True
    else:
        # print('用户名或者密码有误')
        return False


# 调用函数： 添加商品到购物车中
username = input('输入用户名:')
password = input('输入密码:')

islogin = login(username, password)

add_shoppingcart('阿玛尼唇釉')

# 局部和全局
# 全局变量如果是不可变在函数中进行修改需要添加global关键字，
# 如果全局变量是可变的，在函数中修改的时候就不需要添加global
name = '月月'

list1 = [1, 2, 4, 6]


def func():
    name = '蕊蕊'
    print(name)
    print(list1)


def func1():
    global name
    print(name)
    name += '真漂亮！'

    # 修改列表
    list1.append(8)
    print(list1)


def func2():
    name1 = 'lucy'
    name1 += 'hhhh'
    print(name1)  # 自己的

    print(name)


# func1()
#
# func()

func2()
