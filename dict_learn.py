# dictionary 字典
'''
 应用:
 貂蝉 --- ['屠龙刀','手榴弹']  800
 诸葛亮 ---['鹅毛扇','碧血剑','98k枪']  300

 字典：
  特点:
  1. 符号:{}
  2. 关键字: dict
  3. 保存的元素是:key:value  -对


 列表    元组    字典
 []      ()      {}

 list   tuple   dict
 ele     ele   key:value


[].append(8)

element  元素

'''

# 定义

dict1 = {}  # 空字典

dict2 = dict()  # 空字典    list1 = list()  空列表   tuple1= tuple()  空元组

dict3 = {'ID': '93848304309403', 'name': 'lucky', 'age': 18}  # ['7384938493','lucky',18]

# dict4 = dict(('name','lucky'))   # {'name':xxx,'lucky':xxx}
# print(dict4)

dict4 = dict([('name', 'lucky'), ('age', 18)])  # 'name':'lucky','age':18
print(dict4)

dict5 = dict([(1, 2), (4, 5), (6, 8), (9, 0)])
print(dict5)

# 注意：list可以转成字典 但是前提：列表中元素都要成对出现

# 字典的增删改查:

# 增加: 格式:dict6[key]=value
# 特点:  按照上面的格式，如果在字典中存在同名的key，则发生值的覆盖（后面的值覆盖原来的）。
#        如果没有同名的key，则实现的添加功能（key:value添加到字典中）
dict6 = {}

dict6['brand'] = 'huawei'

print(dict6)  # {'brand':'huawei'}

dict6['brand'] = 'mi'

print(dict6)

dict6['type'] = 'p30 pro'

dict6['price'] = 9000

dict6['color'] = '黑色'

print(dict6)
