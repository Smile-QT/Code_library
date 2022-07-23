
# tf.nn.functional.softmax(x,dim = -1)   一般会有设置成dim=0,1,2,-1的情况
# 中的参数dim是指维度的意思，
# 设置这个参数时会遇到0,1，2，-1等情况，特别是对2和-1不熟悉，
# 细究了一下这个问题,查了一下API手册，是指最后一行的意思。

import torch
import torch.nn.functional as F

input = torch.randn(2, 2, 3)
print(input)

# 1. dim=0
# 要注意的是当dim=0时， 是对每一维度相同位置的数值进行softmax运算，举个栗子：
# 从输出结果可以看出，一共2个维度
# 每一个维度（2,3）对应的数值相加为1，例如：
# [0][0][0]+[1][0][0]=0.0159+0.9841=1
# [0][0][1]+[1][0][1]=0.6464+0.3536=1

m = F.softmax(input, dim=0)
print(m)

# 2. dim=1
# 要注意的是当dim=1时， 是对某一维度的列进行softmax运算：
# 从输出结果可以看出，计算的是某一维度中的列，例如：
# 在第1维度中：
# [0][0][0]+[0][1][0]=0.1058+0.8942=1
# 在第2维度中：
# [1][0][0]+[1][1][0]=0.3189+0.6811=1

m = F.softmax(input, dim=1)
print(m)

# 3.
# 要注意的是当dim=2时， 是对某一维度的行进行softmax运算：
# 从输出结果可以看出，计算的是某一维度中的行，例如：
# 在第1维度中：
# [0][0][0]+[0][0][1]+[0][0][2]=0.0042+0.4726+0.5232=1
# 在第2维度中：
# [1][0][0]+[1][0][1]+[1][0][2]=0.2029+0.2015+0.5955=0.9999=1（是等于1的，只是后面还有很多位小数省略了）
m = F.softmax(input, dim=2)
print(m)

# 4. dim=-1
# 要注意的是当dim=-1时， 是对某一维度的行进行softmax运算：
# 从这里可以发现，dim=-1和dim=2的结果是一样的。

m = F.softmax(input, dim=-1)
print(m)


# 总结：
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










