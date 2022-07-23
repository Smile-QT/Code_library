
# 将numpy.ndarray变成一个张量
# torch.from_numpy(ndarray) → Tensor，
# 即 从numpy.ndarray创建一个张量。

import torch
import numpy as np

a = np.array([1, 2, 3])
t = torch.from_numpy(a)
print(type(a))
print(type(t))




























