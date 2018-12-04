from PIL import Image,ImageFont,ImageDraw
import random

#创建底图
Image_source_path = 'd:/addText.jpg'
Image_out = 'd:/watermark.jpeg'
Image_source = Image.open(Image_source_path).convert('RGBA')
width, height = Image_source.size
print("图片宽度是"+str(width))
print("图片高度是"+str(height))
theWord = (random.choice(open(r'd:/Harry.txt').read().split()).strip())
print(theWord)

text=Image.new('RGBA', Image_source.size, (0,0,0,0))
fnt=ImageFont.truetype("c:/Windows/fonts/simhei.ttf", 100)
d=ImageDraw.Draw(text)
#d.text((text.size[0]-80,text.size[1]-30), "水印",font=fnt, fill=(255,255,255,255))
d.text((width/2,height/2), theWord,font=fnt, fill=(255,255,255,255))
out=Image.alpha_composite(Image_source, text)
#out.show()
out.save(Image_out,'png',quality=95)