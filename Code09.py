
# python三种输出格式
# 第一种  python—print(f “{}”) 的用法
a = 1
b = 2
S = a + b
P = a * b
print(f"Sum of a and b is {S}, and product is {P}")

# 第二种
print('S的值：', S)
print('P的值：', P)

# 第三种
print('S的值： {0}，P的值{1} '.format(S, P))
print('S的值： {}，P的值{} '.format(S, P))
print('S的值： {1}，P的值{0} '.format(S, P))


