# Tensor 和 NumPy 变量互相转化
# tuple 和 list 变量相互转化


# 1. Tensor 转 NumPy
import torch
a = torch.ones(6)
b = a.numpy()
print(a.dtype)
print(b.dtype)


# 2. NumPy 数组转 Tensor

import numpy as np
a1 = np.ones(7)
b1 = torch.from_numpy(a1)
print(a1.dtype)
print(b1.dtype)


# 3. list 转 tuple
list01 = [1, 2, 3]
tu01 = tuple(list01)
print(type(tu01))


# 4. tuple 转 list
tu02 = (1, 2, 3, 4)
list02= list(tu02)
print(type(list02))














