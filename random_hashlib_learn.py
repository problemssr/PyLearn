# random 模块

import random

ran = random.random()  # 0~1之间的随机小数
print(ran)

ran = random.randrange(1, 10, 2)  # randrange(start,stop,step)  1~10 step=2 ---> 1,3,5,7,9
print(ran)

ran = random.randrange(1, 10)  # randrange(start,stop,step)  1~10 step=2 ---> 1,3,5,7,9
print(ran)

ran = random.randint(1, 10)
print(ran)

list1 = ['学强', '飞飞', '家伟', '鹏', '阿文']
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)

pai = ['红桃A', '方片K', '梅花8', '黑桃J']
result = random.shuffle(pai)  # 打乱顺序
print(pai)

# 验证码  大小写字母与数字的组合
def func():
    code =''
    for i in range(4):
        ran1= str(random.randint(0,9))
        ran2 = chr(random.randint(65,90))  #
        ran3 = chr(random.randint(97,122))

        r = random.choice([ran1,ran2,ran3])

        code +=r
    return code

code = func()
print(code)

# 加密算法: md5 sha1  sha256
# base64
import hashlib

msg = '于鹏中午一起吃饭去！'
md5 = hashlib.md5(msg.encode('utf-8'))

print(len(md5.hexdigest()))  # b1a0c31ad20f8f982923f61f8003d8a9   32

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(len(sha1.hexdigest()))  # 40

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(len(sha256.hexdigest()))  # 64


password ='123456'

list1 = []

sha256 = hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())

pwd = input('输入密码:')
sha256 = hashlib.sha256(pwd.encode('utf-8'))
pwd = sha256.hexdigest()
print(pwd)
print(list1)
for i in list1:
    if pwd == i:
        print('登录成功！')

