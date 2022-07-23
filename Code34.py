
# 查看张量的维度
# Tensor类的成员函数dim()可以返回张量的维度，shape属性与成员函数size()返回张量的具体维度分量
import torch
f = torch.randn(2, 3)
print(f)
print(f.dim())
print(f.size())
print(f.size(0))
print(f.size(1))
print(f.shape)
print(f.shape)


