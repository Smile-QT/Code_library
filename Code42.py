
# unsqueeze()函数、squeeze()函数介绍

import torch
# 1. unsqueeze()函数
a = torch.ones(3, 4)
b = a.unsqueeze(0)
print(a)
print(b)
print(b.size())

c = a.unsqueeze(1)
print(c)
print(c.size())

# 2. squeeze()函数 只有维度为1时才能去掉
d = a.unsqueeze(1)
print(d)
print(d.size())

e = d.squeeze(1)
print(d)
print(e)
print(e.size())

# 只有维度为1时才能去掉
f = d.squeeze(0)
print(f)
print(f.size())



















