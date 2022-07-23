
# 显示一张图片
import matplotlib.pyplot as plt  # plt 用于显示图片
from PIL import Image

img1 = Image.open("F:/Graduate students grade three/postgraduate studies/first year of postgraduate study/Transformer/softmax.jpg")

#结果展示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
plt.subplot(121)
plt.imshow(img1)
plt.title('图像1')
plt.axis('off')
plt.show()
