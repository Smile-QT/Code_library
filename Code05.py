
# 把list类型和numpy类型转换成tensor类型
import torch
import numpy
from typing import List

image01 = list([1, 2, 3, 4])
image02 = numpy.array([1, 2, 3, 4])
images01 = torch.as_tensor(image01)
images02 = torch.as_tensor(image02)
print(images01)
print(images02)
