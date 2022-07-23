
# PyTorch的 transpose、permute、view、reshape的区别
import torch
# 1.transpose() 和 permute()的区别
# transpose并不改变a本身的形状，将改变的一个副本赋值给b，相当于先拷贝了一份，
# 然后再改变这份拷贝的permute() 和 tranpose() 比较相似，transpose是交换两个维度，permute()是交换多个维度
a = torch.randn(1, 2, 3, 4)
b = a.transpose(1, 2)
print(a)
print(b)
print(a.shape)  # torch.Size([1, 2, 3, 4])
print(b.shape)  # torch.Size([1, 3, 2, 4])

x = torch.randn(2, 3, 5)
y = x.permute(2, 0, 1)
print(y.shape)  # torch.Size([5, 2, 3])


# 2.transpose()和view()
# b和c的形状虽然相同，但内容是不相等的,transpose的改变不等于view的改变
# 一个不同之处在于view()只能对连续的张量进行操作，
# 并且返回的张量仍然是连续的。transpose()既可以在连续张量上操作，也可以在非连续张量上操作。
# 与view()不同，返回的张量可能不再是连续的。
# 连续性的讨论：https://stackoverflow.com/questions/26998223/what-is-the-difference-between-contiguous-and-non-contiguous-arrays/26999092#26999092
a = torch.randn(1, 2, 3, 4)
b = a.transpose(1, 2)
print(a.shape)  # torch.Size([1, 2, 3, 4])
print(b.shape)  # [1, 3, 2, 4]
c = a.view(1, 3, 2, 4)
print(torch.equal(b, c))  # False
print(c.shape)  # torch.Size([1, 3, 2, 4])


# 3.transpose与view 分别对tensor做了什么样的改变
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(x.shape)
y = x.view(3, 2)
print(y.shape)
z = x.transpose(1, 0)
print(z.shape)
print(x)
print(y)
print(z)
# torch.Size([2, 3])
# torch.Size([3, 2])
# torch.Size([3, 2])
# tensor([[1., 2., 3.],
#         [4., 5., 6.]])
# tensor([[1., 2.],
#         [3., 4.],
#         [5., 6.]])
# tensor([[1., 4.],
#         [2., 5.],
#         [3., 6.]])


# 4.reshape()与view()
# reshape返回一个张量，该张量具有与自身相同的数据和元素数量，但具有指定的形状。
# 如果Shape与当前形状兼容，则此方法返回一个view。有关何时可以返回view的信息。
# reshape 封装了 view，view根据规则有时还需要调用contiguous()

# permute().contiguous().view()相当于reshape
# view返回的Tensor底层数据不会使用新的内存，如果在view中调用了contiguous方法，
# 则可能在返回Tensor底层数据中使用了新的内存，PyTorch又提供了reshape方法，
# 实现了类似于 contigous().view()的功能，使用reshape更方便.












