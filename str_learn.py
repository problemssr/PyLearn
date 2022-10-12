# 左移 m<<n m*2的n次方
print(16 << 2)
# 右移 m>>n m/2的n次方
print(16 >> 2)

# 字符串的内建函数： 声明一个字符串，默认可以调用内建函数（系统准备好的一些函数）

# 第一部分： 大小写相关的
# capitalize()  title() istitle()   upper()  isupper()   lower()  islower（）

message = 'zhaorui is a beautiful girl！'

msg = message.capitalize()  # 将字符串的第一个字符串转成大写的标识形式
print(msg)

msg = message.title()  # 返回的是 每个单词的首字母大写的字符串
print(msg)

result = message.istitle()  # 返回的结果是布尔类型的，True False
print(result)

msg = message.upper()  # 将字符串全部转成大写的表示形式
print(msg)

result = msg.lower()  # 将大写全部转小写
print(result)

# 案例：验证码案例

s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0987654321'

print(len(s))  # 求字符串长度 len(str),返回值是一个整型的数值

# 四个随机数
code = ''

import random

# # IndexError: string index out of range   s = 'abc'  print(s[3])
# # index: 0~len(s)-1    0~61
# 产生四位验证码
for i in range(4):
    ran = random.randint(0, len(s) - 1)  # 获取随机数

    code += s[ran]  # code = code + ‘V’   ---》code='V' 不断拼接到code上

print('验证码:' + code)

# 提示用户输入验证码

user_input = input('请输入验证码:')

if user_input.lower() == code.lower():
    print('验证码输入正确！')
else:
    print('验证码错误！')

# 查找相关的,替换

# find()   rfind()  lfind()   index()  rindex()  lindex()   replace()

s1 = 'index lucy lucky goods'

result = 'R' in s1
print(result)

position = s1.find('R')  # 返回值是-1则代表没有找到
print(position)

position = s1.find('l')  # 如果可以找到则返回字母第一次出现的位置
print(position)

# find('要查找的字符',start,end)
p = s1.find('o', position + 1, len(s1) - 5)  # 也可以指定开始位置查找
print(p)

# https://www.baidu.com/img/bd_logo1.png

url = 'https://www.baidu.com/img/bd_logo1.png'

p = url.rfind('/')  # right find  从右侧检索/的位置
print(p)

filename = url[p + 1:]
print(filename)

p = url.rfind('.')

kz = url[p + 1:]
print(kz)

'''
index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常

p = 'hello'.index('x')

print(p)

ValueError: substring not found

'''

# 替换

s1 = 'index lucy lucky goods'

# replace(old,new,[max])
s2 = s1.replace(' ', '#')
print(s2)

s2 = s1.replace(' ', '', 2)
print(s2)

# 字符串内建函数： encode  编码      decode  解码

# 编码：  网络应用  （中文一般会涉及编码问题）

msg = '上课啦！认真听课！'  # 中文的

'''
https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&tn=SE_PclogoS_8whnvm25&sa=ire_dl_gh_logo&rsv_dl=igh_logo_pcs

'''
# gbk 中文   gb2312 简体中文  unicode

result = msg.encode('utf-8')

print(result)  #

# 解码
m = result.decode('utf-8')
print(m)

# 字符串内建函数： startswith()   endswith()  返回值都是布尔类型True False

# startswith判断是否是以xxx开头的，或者 endswith判断是否是以xxx结尾的

# 应用： 文件上传  只能上传图片(jpg,png,bmp,gif)

filename = '笔记.doc'

result = filename.endswith('doc')  # filename是否是以txt结尾的

print(result)

s = 'hello'

result = s.startswith('he')
print(result)

# 文件上传  只能上传图片(jpg,png,bmp,gif)

# path = input('请选择文件:')  # C:\foo\bar\desk_background.jpg

# # 分析： 要上传的文件的路径path----》文件名-----》通过文件名再判断是否是图片类型
# p = path.rfind('\\')

# filename = path[p+1:]  # 通过切片截取出来文件名

# # 判断是否是图片类型?

# if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('bmp'):
# 	print('是图片允许上传！')
# else:
# 	print('不是图片格式，只能上传图片！')

'''
练习：
 给定一个路径，上传文件（记事本txt或者是图片jpg,png）
 如果不是对应格式的，允许重新指定上传文件，
 如果符合上传的规定则提示上传成功

'''

# \n  \r  \'  \"  \t  \\
#
print(r'aksj\kalsf')

while True:
    path = input('请选择文件:')  # C:\foo\bar\desk_background.jpg

    # 分析： 要上传的文件的路径path----》文件名-----》通过文件名再判断是否是图片类型
    p = path.rfind('\\')

    filename = path[p + 1:]  # 通过切片截取出来文件名

    # 判断是否是图片类型?

    if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('txt'):
        print('允许上传！上传成功！')
        break
    else:
        print('不是图片格式和记事本格式，上传错误！')

# isalpha() 是否是字母   isdigit() 是否是数字

s = 'abcd'
result = s.isalpha()
print("result=", result)

s = '6688'

result = s.isdigit()
print(result)

# sum = 0
# for i in range(3): # 0,1,2
# 	num = input('请输入数字:')  # ll

# 	if num.isdigit():
# 		num = int(num)

# 		sum+=num

# print('sum=',sum)

sum = 0
i = 1

# while i<=3:
# 	num = input('请输入数字:')

# 	if num.isdigit():
# 		num = int(num)
# 		sum+=num
# 		print('第{}个数字数字累加成功！'.format(i))
# 		i+=1
# 	else:
# 		print('不是数字！')

# print('sum=',sum)


# join() : '-'.join('abc')   将abc用-连接构成一个新的字符串

new_str = '-'.join('abc')
print(new_str)

# python 列表  list =['a','v','o','9']   数组
list1 = ['a', 'v', 'o', '9']
result = ''.join(list1)  #
print(result)

result = ' '.join(list1)
print(type(result))

# lstrip    rstrip  strip

s = '   hello    '

# s= s.lstrip()  # 去除字符串左侧的空格
# print(s+'8')

# s = s.rstrip()  # 去除右侧的空格
# print(s+'8')

s = s.strip()
print(s + '8')

# split(‘分隔符’，次数)  分割字符串,将分割后的字符串保存到列表中

s = 'hello world hello kitty'

result = s.split(' ', 2)  # 表示按照空格作为分隔符，分割字符串2次
print(result)

n = s.count(' ')  # count(args)  求字符串中指定args的个数
print('个数:', n)

# s='hfdsjkhfdf;lksd;fk'
# s.count('s')

'''
总结：
大小写： lower()  upper()
查找: find()   rfind()
替换: replace()
分割: split()
连接: join()
编码： encode()  decode()的使用
个数： count()
去除空格：  strip()   lstrip()  rstrip() 
用于判断的:
startswith()   开头判断
endswith()     结尾判断
isalpha()      字母判断
isdigit()      数字判断

'''

print('用户名\t密码\t邮箱')
