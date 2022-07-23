
# expand
# 返回tensor的一个新视图，单个维度扩大为更大的尺寸。
# tensor也可以扩大为更高维，新增加的维度将附在前面。 扩大tensor不需要分配新内存，
# 只是仅仅新建一个tensor的视图，其中通过将stride设为0，一维将会扩展位更高维。
# 任何一个一维的在不分配新内存情况下可扩展为任意的数值。
# 使用expand()函数的时候，x自身不会改变，因此需要将结果重新赋值。

import torch
x = torch.Tensor([[1], [2], [3]])
print(x.size())
print(x)

y = x.expand(3, 4)
print(x)
print(y)
print(x.size())
print(y.size())



