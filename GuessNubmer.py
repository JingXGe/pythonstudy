"""
    猜数字小游戏，输入的值大于或者小于随机生成的数后，继续猜，知道猜中为止
"""
# 生成一个随机数
from random import randint

def play():
    random_int = randint(0, 100)
    while True:
        user_guess = int(input("What number did we guess (0-100)"))

        if user_guess == random_int:
            print(f"You found the number ({random_int}). Congrats!")
            break
        if user_guess < random_int:
            print("Your number is less than the number we guessed.")
            continue
        if user_guess > random_int:
            print("Your number is more than the number web guessed.")
            continue


if __name__ == '__main__':
    play()

print("testtopic-github")