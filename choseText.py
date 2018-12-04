import sys
import linecache
import random

#text_source = 'd:/Harry.txt'
#f=open("d:/Harry.txt","r",encoding='gbk', errors='ignore')
#f= open("d:/Harry.txt","r",encoding='gbk')

#a = random.randrange(1, 547) #1-9中生成随机数
#print (a)
#从文件poem.txt中对读取第a行的数据
#theline = linecache.getline(r'd:/Harry.txt', a)
#theword = theline.split()
#random_word =  random.choice(theword)
#print (theword)
print(random.choice(open(r'd:/Harry.txt').read().split()).strip())
a = (random.choice(open(r'd:/Harry.txt').read().split()).strip())

#lines=f.readline()     #按行读取文件中的内容

#for line in lines:     #循环输出读取的内容

#    print(line)