
# 获取excel中指定列的所有数据
# 获取第0列的数据：抖音视频的网址的序号，序号是从1开始的。
# 读取原始excel表中的抖音视频的路径到指定的列表中


import xlrd


filePath = r"F:/reptile/pinglun/Data/xinnongrenjihua.xlsx"  # excel存放的位置，注意地址中只允许”/“这种斜杠，不允许”\“这种斜杠
data = xlrd.open_workbook(filePath)
sheet1 = data.sheet_by_name("Sheet1")   # 取得excel中子表”Sheet1“
zero_col_values = sheet1.col_values(0)  # 获取Sheet1中第0列的数据：抖音视频的网址的序号，序号是从1开始的。

# 将字符串数字，转化成int型的数字，方便之后使用
for i in range(1, len(zero_col_values)):
    zero_col_values[i] = int(zero_col_values[i])

first_col_values = sheet1.col_values(1)  # 获取Sheet1中第1列的数据：抖音视频的网址
