# 爬取一个抖音视频的评论，并将一些表情包删除了
import random
from selenium import webdriver
import time

driver = webdriver.Chrome('D:/YXL/chromedriver_win32/chromedriver.exe')
driver.get('https://www.douyin.com/video/7070128194791197952')  # 电脑端的抖音视频网址
time.sleep(5)
for cunt in range(1, 1000):
    try:
        a = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div/div/div[4]/div['+str(cunt)+']/div/div[2]/p/span/span/span/span/span/span')
    except:
        continue

    try:
        sleep_time = random.randint(10, 15)
        time.sleep(sleep_time)
        print(a.text)
        with open('D:\YXL\Deep Learning\Deep Learning/reptile/test01.txt','a') as file_object:  # 将爬取的评论放在这个文件中
            file_object.write(str(a.text)+'.\n')
        window_scrollBy_number = random.randint(300, 400)
        driver.execute_script('window.scrollBy(0,' + str(window_scrollBy_number) +')')
    except:
        window_scrollBy_number = random.randint(300, 400)
        driver.execute_script('window.scrollBy(0,' + str(window_scrollBy_number) + ')')
        sleep_time = random.randint(10, 15)
        time.sleep(sleep_time)
        print(a.text)
        with open('D:\YXL\Deep Learning\Deep Learning/reptile/test01.txt','a') as file_object:  # 将爬取的评论放在这个文件中
            file_object.write(str(a.text)+'.\n')





