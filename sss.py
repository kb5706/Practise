#print("hello world")

from PIL import Image
#创建底图
Image_source = 'd:/addText.jpg'
Image_sourcetwo = 'd:/other.png'
Image_output = 'd:/out.png'
def carregar_uml(arquivo, variaveis):
    cadastro_uml = {}
    id_uml = 0

    for i in open(arquivo):
        linha = i.split(",")
print(Image_source)
#carregar_uml(r'‪D:/addText.jpg', Image_source)
#carregar_uml(r'‪D:/other.png', Image_sourcetwo)
#carregar_uml(r'‪D:/out.png', Image_output)
print(Image_source)
target = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
#打开头像
nike_image = Image.open(Image_source)
nike_image = nike_image.resize((300, 300))
#打开装饰
hnu_image = Image.open(Image_sourcetwo)
target.paste(nike_image, (0,0))
target.paste(hnu_image,(0,0))
# 分离透明通道
#r,g,b,a = hnu_image.split()
# 将头像贴到底图
#nike_image.convert("RGBA")
#target.paste(nike_image, (0,0))

#将装饰贴到底图
#hnu_image.convert("RGBA")
#target.paste(hnu_image,(0,0), mask=a)
#layer = Image.new('RGBA', nike_image.size,)
#layer.paste(hnu_image,(100,100))
#Image.composite(layer, nike_image, layer)

# 保存图片
target.save(Image_output)

