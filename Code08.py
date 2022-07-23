
# 计算两个数之和
# input 接收的所有数据都会变成字符串
# 所以当接收完数据后，需要对数据进行处理。
def two_numbers_sum01():
    a = int(input('please input a int number: '))
    b = int(input('please input a int number: '))
    c = a + b
    return c


def two_numbers_sum02():
    a = input('please input a int number: ')
    b = input('please input a int number: ')
    c = a + b
    return c


if __name__ == '__main__':
    d = two_numbers_sum01()
    e = two_numbers_sum02()
    print(d)
    print(type(d))
    print(e)
    print(type(e))





