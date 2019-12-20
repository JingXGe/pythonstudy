"""
    program base
"""
#斐波那契数列，Fibonacci series
#两个元素的总和确定了下一个数
a,b = 0,1
while b < 10:
    print(b)
    a,b = b,b+a
    