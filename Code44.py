
# pytorch masked_fill方法简单理解
# masked_fill方法有两个参数，maske和value，mask是一个pytorch张量（Tensor），
# 元素是布尔值，value是要填充的值，填充规则是mask中取值为True位置对应于self的相应位置用value填充。
# masked_fill_(mask, value)
# 用value填充tensor中与mask中值为1位置相对应的元素。mask的形状必须与要填充的tensor形状一致。
# masked_fill_(mask == 0, value)
# 用value填充tensor中与mask中值为0位置相对应的元素。mask的形状必须与要填充的tensor形状一致。

import torch

m = torch.randint(0, 2, (3, 2))
print(m)

t = torch.randint(1, 2, (3, 2))
print(t)

t = t.masked_fill(m == 0, -1e9)  # 这样的操作并不能改变t的值
print(t)

a = t.masked_fill(m, -1e9)
print(a)
