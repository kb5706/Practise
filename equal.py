# coding=utf-8
# int num1 = 0
# int num2 = 0
from random import randint

def isEqual(num1,num2):

    if num1<num2:
        print("too small")
        return False

    if num1>num2:
        print("too big")
        return False

    if num1==num2:
        print("bingo!")
        return True

num = randint(1,100)
print("Guess what I think ?")
bingo =  False
while bingo == False:
    answer = int(input())
    bingo = isEqual(answer,num)