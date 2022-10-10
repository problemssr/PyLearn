# 不重复特点:
list1 = [3, 5, 8, 9, 1, 8, 4, 2, 5, 8, 9]

# 声明集合： set

s1 = set()  # 创建空集合,只能使用set()

s2 = {1, 3, 7}  # 字典： {key:value,key:value,....}  集合 {元素1，元素2，元素3,...}

print(type(s1))
print(type(s2))

# 应用： 如果将一个列表快速去重 set()
s3 = set(list1)
print(s3)  # {1,2,3,4,5,...}

# 增删改查:

# 1. 增加   s1 = set()
s1.add('hello')

s1.add('小猪佩奇')

s1.add('lucy')

print(s1)

# add()  添加一个元素
# update()  可以添加多个元素,

t1 = ('林志玲', '言承旭')
s1.update(t1)  # {'hello','林志玲',....}

print(s1)

s1.add(t1)
print(s1)

# 2. 删除  remove 如果元素存在则删除，不存在则报错keyError    pop  随机删除（一般删除第一个元素）  clear。。。
#   dicard()  类似remove()   在移除不存的元素的时候不会报错。
s1.remove('言承旭')

print(s1)

# s1.remove('道明寺')
# print(s1)

s1.pop()

print(s1)

s1.pop()

print(s1)

s1.clear()  # 清空

print(s1)

'''
  1. 产生10个1~20的随机数，去除里面的重复项
  2. 键盘输入一个元素，将此元素从不重复的集合中删除

'''

import random

# list1= []

# # set1 = set()

# for i in range(10):
# 	ran = random.randint(1,20)
# 	list1.append(ran)   # [3,5,8,1,1]


# # set1.update(list1)  # {3,5,8,1}.update([3,5,8,1,1])
# set1 =set(list1)

# print(list1)
# print(set1)


# num = int(input('输入一个数字:'))


# set1.discard(num)

# print('删除之后结果:',set1)


# 方式二：
# set1= set()

# for i in range(10):
# 	ran = random.randint(1,20)
# 	set1.add(ran)

# print(set1)


# num = int(input('输入一个数字:'))

# set1.discard(num)

# print('删除之后结果:',set1)


# 其他：符号操作
# print(6 in set1)

set2 = {2, 3, 4, 5, 6}
set3 = {2, 3, 4, 5, 6, 7, 8}

print(set2 == set3)  # 判断两个集合中的内容是否相等

# 测试： print(set2 != set3) ??

# （+  * 不支持）   -  &  |

# set4 = set2+set3
# print(set4)


# set5= set2*2
# print(set5)

set4 = set3 - set2  # 差集  difference()
print(set4)

set5 = set3.difference(set2)
print(set5)

# &  交集   intersection()

set6 = set3 & set2
print(set6)

set7 = set3.intersection(set2)

print(set7)

# |  并集  union()  联合

set8 = set3 | set2

print(set8)

set9 = set3.union(set2)

print(set9)

'''
已知两个列表:
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

找出两个列表的不同元素

找出两个列表的共同元素

'''

'''
	已知两个列表:
	l1 = [5,1,2,9,0,3]
	l2 = [7,2,5,7,9]

	找出两个列表的不同元素

	找出两个列表的共同元素

'''

l1 = [5, 1, 2, 9, 0, 3]
l2 = [7, 2, 5, 7, 9]

s1 = set(l1)
s2 = set(l2)

# 对称差集

result = (s1 | s2) - (s1 & s2)

print(result)

result = s1 ^ s2  # 两个列表中不一样元素  symmetric_difference()

print(result)

'''
 difference_update()

	 s1 = s1.difference(s2)
	 print(s1)
     相同
	 s1.difference_update(s2)

 intersection_update()  交集并赋值
 union_update()   并集并赋值
 symmetric_difference_update()  对称差集并赋值

'''

s1.difference_update(s2)

print(s1)

'''
 关键字: set
 作用： 去重


 符号： - & | ^

 内置函数:
  增加: add()  update()
  删除: remove() discard()  pop()  clear()
  运算： difference()  intersection()  union()  symmetric_difference()

'''

# 可变 和 不可变

# 不可变： 对象所指向的内存中的值是不可以改变

# 不可变的类型： int  str  float  元组tuple   frozenset()

num = 10

s1 = 'abc'
print(id(s1))

s1 = 'abcd'
print(id(s1))

t1 = (3, 5, 6)

print(id(t1))

t1 = (3, 5)

print(id(t1))

# 可变的:对象所指向的内存中的值是可以改变

# 可变类型: 字典dict  列表list  集合set   扩展： frozenset() 不可变

list1 = [1, 2, 3, 4, 5]
print(list1, id(list1))

list1.pop()
print(list1, id(list1))

dict1 = {1: 'aa', 2: 'bb'}
print(dict1, id(dict1))

dict1.pop(1)
print(dict1, id(dict1))

'''
  集合 是可变的还是不可变的？

'''

set1 = {3, 5, 6, 8}

print(set1, id(set1))

set1.discard(5)
print(set1, id(set1))

fset = frozenset(set1)  # {3,6,8}

print(fset, id(fset))

fset = frozenset({3, 6})
print(fset, id(fset))
