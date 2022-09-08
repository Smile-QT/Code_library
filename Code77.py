
# 使用python在已存在的excel数据表中的特定位置写入数据
# excel表中的行和列都是从1开始的
import openpyxl as op

filePath = r"F:/reptile\pinglun\Data\xinnongrenjihua02.xlsx"
tableAll = op.load_workbook(filePath)
table1 = tableAll['Sheet1']  # excel中的Sheet1表
table1.cell(2, 3, str(11))  # 第1个位置表示单元格所在的行，第2个位置表示单元格所在的列，第3个位置表示单元格需要写入的内容
tableAll.save(filePath)





