## print("hello world!")

"""
    注释
      注释
    汇率转换器；输入美元显示人民币
"""
# # 1.获取数据
# str_usd = input("请输入美元")
# float_usd = float(str_usd)
# # 2.逻辑处理
# rmb = float_usd * 6.7
#
# # 3.显示结果
# print(rmb)

# print("qtx")
# qtx = input("context")
#
# print(qtx)
#
#
# class_name = "1111"
# stu_name = "zs"
# class_name = stu_name + class_name

# class_name1, class_name2 = "ls", "ww"
# print(class_name1, class_name2)

"""
    分别赋值两个变量；
    将这两个变量值交换；
"""
# 1.赋值
str_a = input("输入第一个值")
str_b = input("输入第二个值")
# # 2.临时变量进行交换
# str_c = str_a
# str_a = str_b
# str_b = str_c
# 2.直接交换
str_a, str_b = str_b, str_a
# 3.输出
print("第一个变量为:" + str_a)
print("第二个变量为:" + str_b)

