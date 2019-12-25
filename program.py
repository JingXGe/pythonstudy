"""
    program base
"""
# 斐波那契数列，Fibonacci series
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, b + a

c, d = 0, 1
while d < 120:
    print(d, end=',')
    c, d = d, d + c

# 判断dog的年龄相当于人类的多少岁
import sys

age_input = input("请输入dog的年龄：")
print("")
try:
    age = int(float(age_input))
except ValueError:
    print("please inport a number!")
    sys.exit(0)

if age <= 0:
    print("wrong age")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄:", human)
# else:
#     print("inport again")
input("点击enter键退出")

# age = input("输入一个数:")
# age1 = float(age)
# print("整数为:", int(age1))

# 输入一个数字判断是否能够整数2或3
num = int(input("请输入一个数字: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2但不能整除3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")
