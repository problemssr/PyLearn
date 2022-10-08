# 声明
names = ['jack', 'tom', 'lucy', 'superman', 'ironman']  # 列表

computer_brands = []

# 增删改查

# 地址

print(id(names))
print(id(computer_brands))

# 查: 通过下标
# 元素获取使用： 下标  索引
print(names[0])
print(names[1])

# 获取最后一个元素
print(names[-1])

print(len(names))

print(names[len(names) - 1])

# 获取第一个元素
print(names[-5])

# 结合循环
# for i in 'hello':
# 	print(i)
print('***************')
for name in names:
    print(name)

# 查询names里面有没有保存超人
for name in names:  # name = jack   name=tom

    if name == 'superman':
        print('有超人在里面！')
        break
else:
    print('没有找到超人在里面！')

# 简便  't' in 'they'  ----> True  False

if 'superman' in names:  # 判断有没有
    print('有超人在里面！')
else:
    print('没有找到超人在里面！')

# 增删改

brands = ['hp', 'dell', 'thinkpad', '支持华为', 'lenovo', 'mac pro', '神州']  # HASEE

# 改
print(brands)

print(brands[-1])

brands[-1] = 'HASEE'  # 赋值  步骤：1.找到（使用下标）  2. 通过=赋值  3.新的值覆盖原有的值

print(brands)

print('-------------------')
# HUAWEI

# for brand in brands:
# 	if '华为' in  brand:
# 		brand= 'HUAWEI'

# print(brands)


for i in range(len(brands)):
    # i是0,1,2,3，。。。 ---》 下标
    if '华为' in brands[i]:
        brands[i] = 'HUAWEI'
        break

print(brands)

# 删除  del  是 delete的缩写

del brands[2]

print(brands)

# 删除 只要是 hp ， mac 都要删除
print('-----------删除---------------')
# l=len(brands)

# for i in range(l):
# 	if 'hp' in brands[i] or 'mac' in brands[i]:
# 		del brands[i]
# 		# break

# print(brands)


l = len(brands)
i = 0
while i < l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        l -= 1  # 长度的减少

    i += 1  # 下标的增加

print(brands)

'''
  They are students
  yews


  words = ['hello','good','apple','world','digit','alpha']

  提示输入一个单词比如：hello，如果输入的单词在列表中则删除

  最后打印删除后的列表


'''

w = 'helloaa'

if 'll' in w:
    print('zai')

'''

  words = ['hello','good','apple','world','digit','alpha']

  提示输入一个单词比如：hello，如果输入的单词在列表中则删除

  最后打印删除后的列表

'''

words = ['hello', 'good', 'gooo', 'world', 'digot', 'alpha']

w = input('请输入一个单词：')

# 方式1：
# if w in words:
# 	print('存在次单词')

#    'abc'  in ['abc','hello','aaaa',..] 内容有没有在列表中存在
#    'go'  in  'good'  判断字符串w有没有出现在word
# for word in words:
# 	if w == word:     # ==   'go'=='good'           in
# 		print('存在此单词！')
# 		break


# for word in words:
# 	if w in word:
# 		del word
# 		break

# print(words)

words = ['hello', 'goods', 'gooo', 'world', 'digot', 'alphago']

w = input('请输入一个单词：')

i = 0  # 表示下标

l = len(words)  # 5

while i < l:  # i<5
    if w in words[i]:
        del words[i]
        l -= 1
        # i-=1
        continue

    i += 1

print(words)

# 字符串切片操作

# s = 'abcdefg'  s[2:5]  --->cde

#  标号：

list1 = ['杨超越', '热巴', '佟丽娅', '杨幂', '赵丽颖', '刘亦菲', '黑嘉嘉', 100, 99.9]

print(list1)

print(list1[3])

# 列表也是支持切片   从左向右

print(list1[3:6])  # 将截取的结果再次保存在一个列表中  ['杨幂','赵丽颖','刘亦菲']

print(list1[-3:-1])

print(list1[::2])  # 步长

print(list1[-5:-1:2])  #

# 反方向  从右向左
print(list1[-1::-1])

print(list1[-1::-2])  # [99.9,'黑嘉嘉','赵丽颖','佟丽娅','杨超越']

# list列表的添加：
# 临时小数据库：list

# 创建一个空列表

girls = ['杨幂']
# quit  表示退出

# 列表的函数使用: append   extends  insert

# append() 末尾追加
# while True:

# 	name = input('请输入你心目中的美女名字:')
# 	if name=='quit':
# 		break

# 	girls.append(name)

# print(girls)


# extend  类似列表的合并
names = ['黑嘉嘉', '孙俪', '巩俐', '王丽坤']

# name = input('请输入你心目中的美女名字:')
# girls.extend(names)


print(girls)

# 符号  +   也可以用于列表的合并

girls = girls + names
print(girls)

# insert   插入

# ['杨幂','黑嘉嘉','孙俪','巩俐','王丽坤']
#   0       1        2      3    4

# append 末尾追加
# insert 指定位置添加
# extend 一次添加多个元素

girls.insert(1, '刘涛')

print(girls)

# 产生10个随机数，将其保存到列表中
'''
步骤：
1. 如何产生随机数
2. 10个数字产生
3. 将产生的随机数放到列表中
4. 打印列表
'''
import random

# random_list=[]  # 用来存放随机数

# for i in range(10):
# 	ran = random.randint(1,20)
# 	# 保存到列表中
# 	random_list.append(ran)

# print(random_list)


# 产生10个不同的随机数，将其保存到列表中
# random_list=[]

# for i in range(10):
# 	ran = random.randint(1,20)

# 	# if ran in random_list：
# 	# 	pass
# 	# else:
# 	# 	random_list.append(ran)

# 	if ran not in random_list:
# 		random_list.append(ran)

# print(random_list)  # 个数不一定是10个

random_list = []

i = 0

while i < 10:
    ran = random.randint(1, 20)

    if ran not in random_list:
        random_list.append(ran)
        i += 1

print(random_list)

# 找出列表中的最大值  max(list) ---->列表中的最大值
max_value = max(random_list)
print(max_value)

min_value = min(random_list)
print(min_value)

print('------------自定义求最大值和最小值---------------')

# 假设列表中的第一个元素就是最大值
mvalue = random_list[0]

minvalue = random_list[0]  # 假设的最小值

for value in random_list:
    # 求最大值
    if value > mvalue:
        mvalue = value
    # 求最小值
    if value < minvalue:
        minvalue = value

print('最大值是:', mvalue, ',最小值是:', minvalue)

# 求和

he = sum(random_list)
print('系统计算求和:', he)

# 声明累加的变量名sum_1
sum_1 = 0

for value in random_list:
    sum_1 += value

print(sum_1)

# 排序: sorted 排序  默认是升序
# sorted(list)  ---> 默认是升序  1,2,3,4,5,6
# sorted(list,reverse=True)   ---->降序   6,5,4,3,2,1

new_list = sorted(random_list, reverse=True)
print(new_list)

# 自己写： 冒泡排序法
