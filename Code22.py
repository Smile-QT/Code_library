
# 可视化显示数据增强后的图片（注意:中文字符显示）
from matplotlib.font_manager import FontProperties
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import numpy as np

mean_nums = [0.485, 0.456, 0.406]
std_nums = [0.229, 0.224, 0.225]
img = Image.open("F:/photo/grocery store/photo01.jpg")
img = transforms.ToTensor()(img)
img = img.numpy()

my_font = FontProperties( size = 12)
# img = img.numpy().transpose((1, 2, 0))  # 转置
img = np.transpose(img, (1, 2, 0))
mean = np.array([mean_nums])
std = np.array([std_nums])
img = std * img + mean  # 还原
img = np.clip(img, 0, 1)  # 限制像素值在0-1之间
plt.imshow(img)
plt.axis('off')
