
# transforms.Resize(x) 将图片短边缩放至x，长宽比保持不变
# transforms.Resize([h, w]) 而一般输入深度网络的特征图长宽是相等的，就不能采取等比例缩放的方式了，需要同时指定长宽
# 例如transforms.Resize([224, 224])就能将输入图片转化成224×224的输入特征图
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

img = Image.open("F:/photo/grocery store/photo01.jpg")
print(img.size)
resize01 = transforms.Resize(224)
resize02 = transforms.Resize([224, 224])
img01 = resize01(img)
img02 = resize02(img)
print(img01.size)
print(img02.size)
