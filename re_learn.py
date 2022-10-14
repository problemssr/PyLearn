# qq = input('输入qq号码')
# if len(qq) >= 5 and qq[0] != '0':
#     print('合法的')
# else:
#     print('不合法的')

import re

msg = '佟丽娅娜扎热巴代斯'

pattern = re.compile('佟丽娅')

result = pattern.match(msg)  # 没有匹配
print(result)

# 使用正则re模块方法： match

s = '娜扎热巴代斯佟丽娅'

result = re.match('佟丽娅', s)  # 只要从开头进行匹配，如果匹配不成功则就返回None
print(result)

result = re.search('佟丽娅', s)  # search 进行正则字符串匹配方法，匹配的是整个字符串
print(result)

print(result.span())  # 返回位置

print(result.group())  # 使用group提取到匹配的内容
print(result.groups())

# a2b h6k
# [] 表示的是一个范围

s = '哈哈3u'

result = re.search('[0-9][a-z]', s)
print(result)

msg = 'abcd7yjkfd8hdf00'

result = re.search('[a-z][0-9][a-z]', msg)  # search 只要有匹配的后面就不会继续进行检索，找到一个匹配的就会停止
print(result.group())

result = re.findall('[a-z][0-9][a-z]', msg)  # findall 匹配整个字符串，找到一个继续向下找一直到字符串结尾
print(result)
# 正则符号

# a7a  a88a a7878a
msg = 'a7aopa88akjgka7878a'

result = re.findall('[a-z][0-9]+[a-z]', msg)
print(result)

# qq号码验证 5~11 开头不能是0
qq = '14944689962'
result = re.match('^[1-9][0-9]{4,10}$', qq)
print(result)

# 用户名可以是字母或者数字_， 不能是数字开头，用户名长度必须6位以上 [0-9a-zA-Z]

username = 'admin001'
result = re.search('^[a-zA-Z]\w{5,}$', username)
print(result)

msg = 'a*py ab.txt bb.py kk.png uu.py apyb.txt'
result = re.findall(r'\w*\.py\b', msg)
print(result)

'''
 总结：
  . 任意字符除(\n)
  ^ 开头
  $ 结尾
  [] 范围  [abc]  [a-z]  [a-z*&￥]

  正则预定义：
  \s  空白 （空格）
  \b 边界
  \d 数字
  \w  word  [0-9a-zA-Z_]

  大写反面 \S  非空格  \D  非数字 。。。

  '\w[0-9]' ---> \w  [0-9] 只能匹配一个字母 

  量词：
   *  >=0
   +  >=1
   ?  0,1

   手机号码正则
   re.match('1[35789]\d{9}$',phone)

  {m} ： 固定m位
  {m,}  >=m
  {m,n}  phone > =m   phone<=n

'''

import re

# 分组
# 匹配数字0-100数字
n = '100'
'''
| 或者  
() 分组 （163|126|qq）  一组
'''
# 改进版
result = re.match(r'[1-9]?\d?$|100$', n)
print(result)

# (word|word|word)  区别   [163] 表示的是一个字母而不是一个单词
# 验证输入的邮箱 163  126  qq
email = '73877884@163.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)
print(result)

# 不是以4、7结尾的手机号码(11位)

phone = '15901018869'
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result.group())

# 爬虫
phone = '010-12345678'

result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result)

# 分别提取
print(result.group())
# () 表示分组  group(1) 表示提取到第一组的内容   group(2)表示第二组的内容
print(result.group(1))
print(result.group(2))

#
msg = '<html><h1>abc</h1>'
msg1 = '<h1>hello</h1>'

result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>', msg)
print(result)
print(result.group(1))

# number
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg1)
print(result)
print(result.group(1))
print(result.group(2))

#
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print(result)

print(result.group(1))
print(result.group(2))
print(result.group(3))

import re

# 起名的方式:  (?P<名字>正则) （？P=名字）
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

'''
 分组：()   ---> result.group(1) 获取组中匹配内容  
       在分组的时候还可以结合 |
       result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
        print(result)

 不需要引用分组的内容：
    result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>', msg)
    print(result)
    print(result.group(1))
引用分组匹配内容:
    1.number   \number 引用第number组的数据
        msg = '<html><h1>abc</h1></html>'
        result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
        print(result)

    2.?P<名字>
        msg = '<html><h1>abc</h1></html>'
        result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
        print(result)
        print(result.group(1))


    re模块：
    match    从开头匹配一次
    search   只匹配一次
    findall  查找所有
    sub(正则表达式，'新内容'，string)   替换
    split   result = re.split(r'[,:]','java:99,python:95')   在字符串中搜索如果遇到:或者,就分割
            将分割的内容都保存到列表中了
'''


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


# result = re.sub(r'\d+','90','java:99,python:95')
# print(result)


result = re.sub(r'\d+', func, 'java:99,python:95')
print(result)

result = re.split(r'[,:]', 'java:99,python:95')
print(result)


import re

# 默认是贪婪的,如果想将贪婪模式变成非贪婪模式
msg = 'abc123abc'

result = re.match(r'abc(\d+?)', msg)

print(result)

path = '<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=30a7526a9282d158bb8259b9b00b19d5/704bde177f3e67092893917b35c79f3dfadc55f5.jpg" size="2227636" changedsize="true" width="560" height="840" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'

result = re.match(r'<img class="BDE_Image" src="(.*?)"', path)
# print(result.group(1))
image_path = result.group(1)
import requests

response = requests.get(image_path)

with open('aa.jpg', 'wb') as wstream:
    wstream.write(response.content)
