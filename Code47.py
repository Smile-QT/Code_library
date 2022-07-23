

# 列表
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 张量（把列表转化成张量）

# 1.访问列表中的值
print( list1[0] )
print( list1[-1] )
print(list1[0:3])  # 输出'Google', 'Runoob', 1997, 不包括3对应的数据
print(list1[1:-1]) #  'Runoob', 1997 ，不包括-1对应的数据

# 2.修改列表中的值
list1[2] = 2001
print(list1[2])
list1.append('Baidu')
print(list1)



# 3.删除列表元素
del list1[3]
print(list1)







































