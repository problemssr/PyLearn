# Python 基础

## 1.初识python

## 2.字符串

```python
总结：
大小写： lower()
upper()
查找: find()
rfind()
替换: replace()
分割: split()
连接: join()
编码： encode()
decode()
的使用
个数： count()
去除空格：  strip()
lstrip()
rstrip()
用于判断的:
startswith()
开头判断
endswith()
结尾判断
isalpha()
字母判断
isdigit()
数字判断
```

## 3.列表，字典，元组，集合

```markdown
回顾:
数据类型:
字符串： 声明:
''
""
''' '''

符号:
+
*
in not in is not is
[]

获取字符串元素:

s = 'hello' s[0] ~ s[len(s)-1]

切片:
s[start:end[:step]]  包前不包后

内置函数:
lower()  upper()
replace()
split()  
find()  rfind()  lfind()
strip()  lstrip()  rstrip()
join()
isalpha()  isdigit()
...

‘容器’:

列表: list 特点:  保存多个元素，元素有顺序。可以通过下标找到对应的元素。  
可以增加，删除，修改元素，查询 内置函数:
append extend insert remove pop clear , del sort reverse index count

元组: tuple 特点: 保存多个元素。 不可以增加，删除，修改元素。但是可以查询元素

内置函数: index count 支持下标操作： t= （1,2,3） t[0],t[1:]

字典: dict 特点: 键值对保存元素。 键是唯一的，而值不唯一。 可以支持对键值对的增删改查 内置函数:
增加(修改)键值对:  dict1={} dict1[key]=value  
删除键值对: dict1.pop()   dict1.popitem()   dict1.clear()
查询: items()  values()  keys()

集合: set 关键字 无序的不重复的元素 作用: 不重复特点

```

## 3.可变元素和不可变元素，函数

```markdown
集合： list tuple ---》set()
无序不重复的序列，集合 无序 ---》 跟下标相关

s ={1,2,3,4,5} ---->s[1]

for i in s:
print(i)

内置函数： 添加： add update 删除: remove discard pop clear

运算相关函数：

- difference()
  | union()
  & intersection()
  ^ symmetric_difference()

可变和不可变： 可变: 地址不变里面内容改变 list dict set 不可变: 只要内容改变，必须改变地址 int str float tuple frozenset

类型转换:
str ---> list set ... 相互的转换

list ---> set tuple dict 相互的转换

函数:

增加代码的复用性，减少了代码冗余

def 函数名([参数,...]):
函数体（重复性代码）

没有参数:

def add():
result = 1+3 print(result)

调用:
add()   ---> 4

有参数:

def add(a,b):
result = a+b print(result)

调用:
add(1,3)
add(5,6)
add(100,29)

总结:

1.参数的种类： 
2.返回值return
3.函数间相互调用 
4.局部和全局变量

```

## 4.函数

```python
集合：
 list  tuple ---》set()
 无序不重复的序列，集合
 无序 ---》 跟下标相关

 s ={1,2,3,4,5}  ---->s[1]

 for i in s:
    print(i)

内置函数：
添加： add update
删除: remove  discard  pop  clear

运算相关函数：
-  difference()
|  union()
&  intersection()
^  symmetric_difference()

可变和不可变：
可变: 地址不变里面内容改变   list  dict  set
不可变: 只要内容改变，必须改变地址   int  str  float  tuple frozenset


类型转换:
str ---> list  set ...  相互的转换

list ---> set tuple dict  相互的转换



函数:

增加代码的复用性，减少了代码冗余

def 函数名([参数,...]):
    函数体（重复性代码）


没有参数:

def add():
    result = 1+3
    print(result)

调用:
add()   ---> 4


有参数:

def add(a,b):
    result = a+b
    print(result)

调用:
add(1,3)
add(5,6)
add(100,29)



总结:

1.参数的种类：
2.返回值return
3.函数间相互调用
4.局部和全局变量

```

