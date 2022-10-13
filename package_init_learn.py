'''
 __init__.py文件
当导入包的时候，默认调用__init__.py文件
作用:
1. 当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py文件中
2. 此文件中函数，变量等的访问，只需要通过：包名.函数....
3. 结合__all__=[通过* 可以访问的模块]
'''

# import user  # ---------> user的__init__
#
# # from user.models import User
#
# user.create_app()
# user.printA()

# from 模块 import *     表示可以使用模块里面的所有内容，如果没有定义__all__所有的都可以访问，
#                        但是如果添加上了__all__,只有__all__=['',''] 列表中可以访问的

# from 包 import *   表示该包中内容（模块）是不能访问，就需要在__init__.py文件中定义__all__ =[可以通过*访问的模块]
from user import *

user = models.User('admin', '123456')
user.show()

print(test.MAX)
