# 语法错误和异常
# 语法错误：
# while True:
#     print('-------')

# number = 100
#
#
# def func():
#     global number
#     number += 1


# 异常：程序运行的时候报出来的。xxxError
# def chu(a, b):
#     return a / b
#
#
# x = chu(4, 2)  # ZeroDivisionError: division by zero
# print('--------------->', x)

# 异常处理:
'''
格式:
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会被执行的代码]


情况1：
  try:
     有可能会产生多种异常
  except 异常的类型1：
        print（。。。。）
  except 异常类型2:
       pass

'''


def func():
    try:
        n1 = int(input('输入第一个数字:'))
        n2 = int(input('输入第二个数字:'))
        # + 加法
        per = input('输入运算符号(+ - * /):')

        result = 0
        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        else:
            print('符号输入有误！')

        print('结果是:', sum)
    except ZeroDivisionError:
        print('除数不能为零！！！！')
    except ValueError:
        print('必须输入数字！！！！')
    except FileNotFoundError:
        pass
    except NameError:
        pass
    except Exception:
        pass

func()

print('------------>')


'''
格式:
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会被执行的代码]


情况1：
  try:
     有可能会产生多种异常
  except 异常类型1：
        print（。。。。）
  except 异常类型2:
       pass
  except Exception:
       pass

  如果是多个except，异常类型的顺序需要注意，最大的Exception要放到最后



情况2：获取Exception的错误原因
try:
     有可能会产生多种异常
  except 异常类型1：
        print（。。。。）
  except 异常类型2:
       pass
  except Exception as err:
       print(err)  ----> err的内容就是错误原因：

   pop from empty list  ---》 从空的列表中删除内容
   。。。

'''


def func():
    try:
        n1 = int(input('输入第一个数字:'))
        n2 = int(input('输入第二个数字:'))
        # + 加法
        per = input('输入运算符号(+ - * /):')

        result = 0
        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        else:
            print('符号输入有误！')

        print('结果是:', result)

        # 操作列表
        list1 = []
        list1.pop()  #

        # 文件操作
        with open(r'c:\p1\aa.txt', 'r') as  wstream:
            print(wstream.read())

    except ZeroDivisionError:
        print('除数不能为零！！！！')
    except ValueError:
        print('必须输入数字！！！！')
    except Exception as err:
        print('出错啦！', err)


func()

print('------------>')


# 异常
'''
 情况3：try...except..(多个except)...else
  try:
     有可能有异常的代码
  except 类型1:
      pass
      ..
  else:
     如果try中没有发生异常则进入的代码

注意： 如果使用else则在try代码中不能出现return
'''


def func():
    try:
        n1 = int(input('输入数字:'))
        print(n1)
        return 1
    except ValueError:
        print('必须是数字....')
        return 2
    else:
        print('数字输入完毕！')   # 没有异常才会执行的代码块


# 调用函数
func()

# 异常情况4
'''
# 文件操作  stream = open(...)   stream.read()   stream.close()
# 数据库操作  close()
try；
   pass
except:
   pass
finally:
   pass

'''


def func():
    stream = None

    try:
        stream = open(r'c:\p1\aa1.txt')
        container = stream.read()
        print(container)
        stream.close()
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('------finally-----')
        if stream:
            stream.close()
        # return 3


x = func()
print(x)


# 抛出异常 raise

# 注册 用户名必须6位
def register():
    username = input('输入用户名:')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是:', username)


try:
    register()
except Exception as err:
    print(err)
    print('注册失败！')
else:
    print('注册成功！')
    # print(a)