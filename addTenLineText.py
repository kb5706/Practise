from PIL import Image,ImageFont,ImageDraw
import random


Image_source_path = 'd:/addText3.jpg'        #创建底图
Image_out = 'd:/watermark'             #结果图
Image_source = Image.open(Image_source_path).convert('RGBA')  #地图转换为rgba模式的对象
# width, height = Image_source.size
# print("图片宽度是"+str(width))
# print("图片高度是"+str(height))
theLine = ""
theWord = ""


for k in range(0,50):
    theLine = ""

for i in range(1,11):
       # theLine = ""
        for j in range(0,i):
            theWord = (random.choice(open(r'd:/Harry.txt').read().split()).strip()) #随机选单词
            print(theWord)
            theLine += theWord+" "   #拼接
        text=Image.new('RGBA', Image_source.size, (0,0,0,0))        #创建新图像text，模式、尺寸、颜色，4个0是全黑
        fnt=ImageFont.truetype("c:/Windows/fonts/simhei.ttf", 30)    #定义字体fnt
        d=ImageDraw.Draw(text)          #创建绘图对象d,

        theLine = theLine + '\n'               #换行
        d.text((20,20), theLine,font=fnt, fill=(255,255,255,255))      #定义水印的位置，内容，字体，颜色
        out=Image.alpha_composite(Image_source, text)           #加水印
out.save(Image_out+str(k)+'.jpg','png')            #输出

