'''
在python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件（.py）就是一个模块（module），
模块名就是文件名去掉后缀py。
这样做的好处是：
- 提高代码的可复用、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
- 解决了命名冲突，不同模块中相同的命名不会冲突

常用标准库：

| 标准库          | 说明                 |
| --------------- | -------------------- |
| builtins        | 内建函数默认加载     |
| math            | 数学库               |
| random          | 生成随机数           |
| time            | 时间                 |
| datetime        | 日期和时间           |
| calendar        | 日历                 |
| hashlib         | 加密算法             |
| copy            | 拷贝                 |
| functools       | 常用的工具           |
| os              | 操作系统接口         |
| re              | 字符串正则匹配       |
| sys             | Python自身的运行环境 |
| multiprocessing | 多进程               |
| threading       | 多线程               |
| json            | 编码和解码 JSON 对象 |
| logging         | 记录日志，调试       |

1. 自定义模块
2. 使用系统一些模块

导入模块:
1. import 模块名
    模块名.变量    模块名.函数    模块名.类
2. from 模块名 import 变量 | 函数 | 类
    在代码中可以直接使用变量，函数，类
3. from 模块名 import *
   该模块中所有的内容
   但是如果想限制获取的内容，可以在模块中使用__all__=[使用*可以访问到内容]
4. 无论是import还是from的形式，都会将模块内容进行加载
   如果不希望其进行调用。就会用到__name__
   在自己的模块里面__name__叫： __main__
   如果在其他模块中通过导入的方式调用的话：__name__: 模块名

'''
list1 = [4, 2, 7, 8, 9]

# 导入模块  import 模块名
# import calculate
#
# # 使用模块中的函数  模块名.变量    模块名.函数    模块名.类
# result = calculate.add(*list1)
# print(result)
#
# # 使用模块变量
# print(calculate.number)
#
# # 使用模块中类
# cal = calculate.Calculate(88)
# cal.test()
#
# calculate.Calculate.test1()

from calculate import *

# from calculate import number

result = add(*list1)
print(result)

sum = result + number
print(sum)

c = Calculate(80)
c.test()
