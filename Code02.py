# 将张量保存为图片
import torch
from torchvision import transforms

toPIL = transforms.ToPILImage()  # 这个函数可以将张量转为PIL图片，由小数转为0-255之间的像素值
img = torch.randn(3, 128, 64)
pic = toPIL(img)
pic.save('C:\LB\Restormer-masterpyV3\YXL/random.jpg')
