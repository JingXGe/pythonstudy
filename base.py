"""
    python基础学习
"""

# 元组
# 元组的元素不能修改但能连接组合，不能删元素但能删除整个元组，元组使用小括号列表使用方括号
tup1 = ('Gggole', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 9, 7)
tup3 = "a", "b", "c", "d"
type(tup3)
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当成运算符使用

print("tup1[0]:", tup1[0])
print("tup2[1:7]:", tup2[1:7])
# 截取时，只包含前不包含后
length = len(tup2)
print(length)
maxtup = max(tup3)
print(maxtup)
# 字母也可以比较大小

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']:", dict['Name'])
print("dict['Age']:", dict['Age'])

dict['Age'] = 8
dict['School'] = "python base"
print("dict['Age']:", dict['Age'])
print("dict['School']:", dict['School'])
del dict['Name']  # 删除键
dict.clear()  # 清空字典
del dict  # 删除字典
