# 批量爬取抖音评论
# chrome驱动程序选择网址：https://blog.csdn.net/python_TB/article/details/124303116


import random
from selenium import webdriver
import time
import xlrd
import openpyxl as op


#########################################################################################################################################

filePath = r"C:\YXL\lijiawen\reptile\pinglun\Data/xinnongrenjihua02.xlsx"
data = xlrd.open_workbook(filePath)

sheet1 = data.sheet_by_name("Sheet1")   # 按名获取该文件中的表格

zero_col_values = sheet1.col_values(0)  # 获取第1列的数据：抖音视频的网址的序号，序号是从1开始的。
# 将字符串数字，转化成int型的数字，方便之后使用
for i in range(1, len(zero_col_values)):
    zero_col_values[i] = int(zero_col_values[i])

first_col_values = sheet1.col_values(1)  # 获取第2列的数据：抖音视频的网址


#########################################################################################################################################

for j in range(1, len(first_col_values)):

    driver = webdriver.Chrome('C:/Users/admin/anaconda3/envs/pytorchYXL/chromedriver_win32_v1/chromedriver.exe')  # chrome驱动程序存放的位置
    douying_vedio_path = first_col_values[j]
    douyingshipingxuhao_pinglunsuoxiehangshu = zero_col_values[j]

    driver.get(douying_vedio_path)  #网页版抖音的网址
    sleep_time_01 = random.random()
    time.sleep(sleep_time_01)
    pinglun_numbers = 0
    for cunt in range(1, 5000):
        # 每一个视频只是爬取30条评论
        if pinglun_numbers == 30:
            # driver.close()
            break
        # 第一个try except，是为了跳过那些不是文字评论的内容，比如有的评论是表情包或者是图片
        try:
            a = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[5]/div/div/div[3]/div['+str (cunt) +']/div/div[2]/div[1]/p/span/span/span/span/span/span')  # 需要爬的评论
            sleep_time = random.random()
            time.sleep(sleep_time)
        except:
            continue

        # 当a中捕获的字符串长度为6时，结束本次运行，并读取下一条评论
        if int(len(str(a.text))) < 6:
            window_scrollBy_number = random.randint(100, 150)
            driver.execute_script('window.scrollBy(0,' + str(window_scrollBy_number) + ')')  # 拖动滚动条，里面是在左右和竖直方向上滚动的像素值，为了防止抖音察觉到我在爬评论，所以把滚动的像素值设置成随机值
            continue

        # 这是把爬下来的评论存放在文件中
        tableAll = op.load_workbook(filePath)
        table1 = tableAll['Sheet1']
        table1.cell(douyingshipingxuhao_pinglunsuoxiehangshu + 1, pinglun_numbers + 3, str(a.text))
        tableAll.save(filePath)



        pinglun_numbers = pinglun_numbers + 1
        sleep_time = random.random()
        time.sleep(sleep_time)  # 等待程序将评论写进word中，且为了让a读取到评论。
        print(a.text)
        print(pinglun_numbers)
        window_scrollBy_number = random.randint(100, 150)
        driver.execute_script('window.scrollBy(0,' + str(window_scrollBy_number) +')')  # 拖动滚动条，里面是在左右和竖直方向上滚动的像素值，为了防止抖音察觉到我在爬评论，所以把滚动的像素值设置成随机值






