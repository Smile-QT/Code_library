
# append、extend、expand()函数详解
# a.append(b)：是将b原封不动的追加到a的末尾上，会改变a的值，其中，b可为列表、元组、字符串、一串数 / 字符 / 字符串
# a.extend(b)：是将b拆开后追加到a的末尾上，会改变a的值，其中，b可为列表、元组、字符串、一串数/字符/字符串


# 1. append
# a.append(b)：是将b原封不动的追加到a的末尾上，会改变a的值，其中，b可为列表、元组、字符串、一串数/字符/字符串

# ①列表
a = [1, 2, 3]
b = [4, 5]
a.append(b)
print(a)  # 输出：[1, 2, 3, [4, 5]]

# ②元组
a = [1, 2, 3]
b = (4, 5)
a.append(b)
print(a)  # 输出：[1, 2, 3, (4, 5)]

# ③字符串
a = [1, 2, 3]
b = 'string'
a.append(b)
print(a)  # 输出：[1, 2, 3, 'string']

# ④一串数/字符/字符串:会将b转化为元组追加到a的末尾上
# (1)一串数
a = [1, 2, 3]
b = 4, 5
a.append(b)
print(a)  # 输出：[1, 2, 3, (4, 5)]

# (2)一串字符
a = [1, 2, 3]
b = 'l', 'a', 'n'
a.append(b)
print(a)  # 输出：[1, 2, 3, ('l', 'a', 'n')]

# (3)一串字符串
a = [1, 2, 3]
b = 'lan', 'tian'
a.append(b)
print(a)  # 输出：[1, 2, 3, ('lan', 'tian')]

# 2. extend:   a.extend(b)：是将b拆开后追加到a的末尾上，会改变a的值，其中，b可为列表、元组、字符串、一串数/字符/字符串:

# ①列表
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)  # 输出：[1, 2, 3, 4, 5]

# ②元组
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a)  # 输出：[1,2,3,4,5]

# ③字符串
a = [1, 2, 3]
b = 'lantian'
a.extend(b)
print(a)  # 输出：[1, 2, 3, 'l', 'a', 'n', 't', 'i', 'a', 'n']

# ④一串数/字符/字符串
# (1)一串数
a = [1, 2, 3]
b = 4, 5
a.extend(b)
print(a)  # 输出：[1, 2, 3, 4, 5]

# (2)一串字符
a = [1, 2, 3]
b = 'l', 'a', 'n', 't', 'i', 'a', 'n'
a.extend(b)
print(a)  # 输出：[1, 2, 3, 'l', 'a', 'n', 't', 'i', 'a', 'n']

# (3)一串字符串
a = [1, 2, 3]
b = 'lan', 'tian', 'n'
a.extend(b)
print(a)  # 输出：[1, 2, 3, 'lan', 'tian', 'n']


# 3. expand 返回tensor的一个新视图，单个维度扩大为更大的尺寸。tensor也可以扩大为更高维，新增加的维度将附在前面。
# 扩大tensor不需要分配新内存，只是仅仅新建一个tensor的视图，其中通过将stride设为0，一维将会扩展位更高维。任何一个一维的在不分配新内存情况下可扩展为任意的数值。
import torch
x = torch.Tensor([[1], [2], [3]])
print(x)
print("x.size():", x.size())

y = x.expand(3, 4)
print(y)
print(y.size())








