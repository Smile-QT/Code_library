
# 张量转化成数组
import numpy as np
import torch

a = torch.Tensor([0,1]) # 如果参数不是一个list，而是一个int，将会返回该int长的内容未定义的Tensor
print(type(a))
a = a.numpy()
print(type(a))


# 数组转化成张量
b = np.random.rand(3)
print(type(b))
b = torch.from_numpy(b)
print(type(b))


# 列表转化成张量
c = [1, 2]
print(type(c))
c = torch.tensor(c)
print(type(c))



# 列表转化成数组
d = [1, 2]
print(type(d))
d = np.array(d)
print(type(d))









