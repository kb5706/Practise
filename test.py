import random
from skimage import io

#result = (random.choice(open(r'd:/Harry.txt').read().split()).strip())
#result = (random.choice(open(r'd:/Harry.txt').read().split()))
#result = (random.choice(open(r'd:/Harry.txt').read()))

# result = (open(r'd:/Harry.txt').read().split())
# print(result)

# l = [1, 1, 2, 3, 5, 8, 13]
# print (l)

# from random import choice
#
# direction = ['left','middle','right']
# print("which direction do you want?")
# print("left,middle or right?")
# you = input()
# print("you kicked "+ you)
# computer = random.choice(direction)
# if you != computer :
#     print("you win!")
# else:
#     print("you lose")

# word = 'helloworld'
# print(word[5:7])
#print (word[:-5])

#print (word[:])
# for c in word:
#     print(c)
#     print(word[0])
#
#     print(word[-2])

f1 = open('test.txt')
f2 = open('test.jpg')
data1 = f1.read()
data2 = io.imread('test.jpg')
f1.close()
f2.close()
out1 = open('out.txt','w')
out1.write(data1)
out1.close()
out2 = open('out.jpg','wb')
out2.write(data2)
out2.close()

