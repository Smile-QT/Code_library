
# enumerate
# enumerate()是python的内置函数
# enumerate在字典上是枚举、列举的意思
# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
# enumerate多用于在for循环中得到计数
# 当enumerate的参数是字典时，enumerate提取的是字典的键，不会提取字典的值
tgt_vocab = {'P': 0, 'i': 1, 'want': 2, 'a': 3, 'beer': 4, 'coke': 5, 'S': 6, 'E': 7, '.': 8}
idx2word = {i: w for i, w in enumerate(tgt_vocab)}
print(idx2word)


list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print(index, item)


