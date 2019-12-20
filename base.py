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

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 可去重
print('orange' in basket)
print('crabgrass' in basket)
print('glass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)

print(a - b)  # a中包含而b中不包含的元素

a.add('t')
print(a)  # 添加元素

a.update({1, 3})
print(a)
a.update([5, 4], [9, 6])
print(a)
# 添加元素，可以是列表/元组/字典

a.remove(5)
print(a)
a.discard(10)
print(a)
# 删除元素，无此元素前者会报错后者不报错
a.pop()
print(a)  # 随机删除一个元素

thisset = set(("google", "runoob", "taobao", "facebook"))
x = thisset.pop()
print(thisset)
print(x)
# set集合的pop方法会对集合进行无序的排列，然后将这个排列集合的左面第一个元素删除

print(len(thisset))  # 计算集合个数

myset = set(("google", "runoob", "taobao"))
myset.clear()
print(myset)
# 清空集合
print("google" in thisset)
# 判断元素是否存在