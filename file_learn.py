# 文件操作:
'''
 文件上传
 保存log

系统函数：
 open(file,mode,buffering,encodeing)

 读:
   open（path/filename,'rt'）---->返回值：stream (管道)

   container = stream.read()  ---->读取管道中内容

   注意： 如果传递的path/filename有误，则会报错：FileNotFoundError
    如果是图片则不能使用默认的读取方式,mode = 'rb'

    总结:
    read()  读取所有内容
    readline() 每次读取一行内容
    readlines() 读取所有的行保存到列表中
    readable()  判断是否可读的

'''

stream = open(r'C:\p1\aa.txt')

# container = stream.read()
# print(container)

result = stream.readable()  # 判断是否可以读取  True  False
print(result)

# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break


lines = stream.readlines()  # 保存到列表中
print(lines)
for i in lines:
    print(i)

stream = open(r'C:\p1\girl.jpg', 'rb')

container = stream.read()
# print(container)

# 写文件
'''
stream = open(r'c:\p1\aa.txt', 'w')
mode 是’w‘ 表示就是写操作  每次都会将原来的内容清空，

方法:
     write(内容)   然后写当前的内容
    writelines(Iterable)  没有换行效果
    stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])  ---》自己加

如果mode='a'


'''

stream = open(r'c:\p1\aa.txt', 'a')

# s = '''
# 你好！
#     欢迎来到澳门博彩赌场，赠送给你一个金币！
#                 赌王: 高进
#
# '''

result = stream.write('hello')
# print(result)

stream.write('龙五')

stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])

stream.write('僵尸先生')

stream.close()  # 释放资源

# stream.write('龙五2号')


# 文件的复制
'''
原文件： c:\p1\girl.jpg
目标文件： c:\p2\girl.jpg

with 结合open使用，可以帮助我们自动释放资源

'''
# stream = open(r'c:\p1\girl.jpg', 'rb')

with open(r'c:\p1\girl.jpg', 'rb') as stream:
    container = stream.read()  # 读取文件内容

    with open(r'c:\p2\girl.jpg', 'wb') as wstream:
        wstream.write(container)

print('文件复制完成！')

# 模块： os.py
import random

'''
os.path:
os.path.dirname(__file__)获取当前文件所在的文件目录（绝对路径）
os.path.join(path,'')  返回的是一个拼接后的新的路径

'''

import os

# print(os.path)
# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录（绝对路径）
# print(path)
# print(type(path))
# result = os.path.join(path, 'a1.jpg')
# print(result)
# p1\girl.jpg ---->保存在当前文件所在的目录

with open(r'c:\p1\girl.jpg', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    filename = file[file.rfind('\\') + 1:]  # 截取文件名

    path = os.path.dirname(__file__)
    path1 = os.path.join(path, filename)

    with open(path1, 'wb') as wstream:
        wstream.write(container)

# os.path里面函数
# os中函数：
import os

dir = os.getcwd()
print(dir)

all = os.listdir(r'c:\p1')  # 返回指定目录下的所有的文件和文件夹,保存到列表中
print(all)

# 创建文件夹
if not os.path.exists(r'c:\p3'):
    f = os.mkdir(r'c:\p3')
    print(f)

# f = os.rmdir(r'c:\p3')  # 只能删除空的文件夹  OSError: [WinError 145] 目录不是空的。: 'c:\\p3'
# print(f)

# f = os.removedirs(r'c:\p3')
# print(f)

# os.remove(r'c:\p3\p4\aa.txt')

# 删除p4文件夹
# path = r'c:\p3\p4'
#
# filelist = os.listdir(path)   #['a1.doc', 'aa.txt', 'girl.jpg']
#
# for file in filelist:
#     path1 = os.path.join(path,file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
#
# print('删除成功！')

# 切换目录

path = os.getcwd()
print(path)

f = os.chdir(r'c:\p1')
print(f)

path = os.getcwd()
print(path)

'''
os模块下方法:
os.getcwd()  获取当前目录
os.listdir()  浏览文件夹
os.mkdir()  创建文件夹
os.rmdir()  删除空的文件夹
os.remove()  删除文件
os.chdir()  切换目录

'''




import os

src_path = r'c:\p1'
target_path = r'c:\p3'


def copy(src_path, target_path):  # 'c:\p1'
    # 获取文件夹里面内容
    filelist = os.listdir(src_path)  # ['a1.doc', 'aa.txt', 'girl.jpg', 'pp']   ['p1.txt','p2.txt']
    # 变量列表
    for file in filelist:
        # 拼接路径
        path = os.path.join(src_path, file)  # c:\p1\pp\p1.txt
        # 判断是文件夹还是文件
        if os.path.isdir(path):  # path = ‘c:\p1\pp’
            # 递归调用copy
            target_path1 = os.path.join(target_path, file)
            os.mkdir(target_path1)
            copy(path, target_path1)

        else:
            # 不是文件夹则直接进行复制
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完成！')


# 调用copy
copy(src_path, target_path)


# 持久化保存：文件
# list 元组，字典---->内存

# 用户注册
def register():
    username = input('输入用户名:')
    password = input('输入密码:')
    repassword = input('输入确认密码:')

    if password == repassword:
        # 保存信息
        with open(r'c:\p1\book\users.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, password))

        print('用户注册成功！')
    else:
        print('密码不一致！')


# 用户登录
def login():
    username = input('输入用户名:')
    password = input('输入密码:')

    if username and password:
        # 打开文件查看
        with open(r'c:\p1\book\users.txt')  as rstream:
            # 逐行读取内容
            while True:
                # 读取一行内容
                user = rstream.readline()  # admin 123456\n
                # 判断有没有读取到内容
                if not user:
                    print('用户名或者密码输入有误！')
                    break
                # 构造比较格式
                input_user = '{} {}\n'.format(username, password)
                # 如果用户输入的跟文件中的内容一致则认为用户登录成功
                if user == input_user:
                    print('用户登录成功！')
                    break


def show_books():
    print('---------图书馆里面的图书有:----------')
    with open(r'c:\p1\book\books.txt', 'r') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')  # 因为读取的内容中有\n 所以取消print中自带的末尾换行

# 调用函数:
# register()
# login()
# show_books()
