
# range torch.range torch.arange区别
# torch.range torch.arange最后的结果的张量

import torch
y = torch.range(1, 6)
print(y)
print(y.dtype)
print(y.type())


z = torch.arange(1, 6)
print(z)
print(z.dtype)
print(z.type())


a = list()
a = range(5)
for i in a:
    print(i)
