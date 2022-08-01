# Tensor 和 NumPy变量互相转化
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















