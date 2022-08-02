# X轴向左边平移图像大小的1/5，Y轴向下平移图像大小的的1/4

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#@Time : 2022/6/2 13:36
#@Author : Smile
#@File : code1_2.py
#@Software: PyCharm
@Description:
"""

# 使用opencv处理图片
import cv2
import numpy as np
from matplotlib import pyplot as plt


def image_panning(src_img_path: str, result_img_path: str, Horizontal_distance_rate: float, vertical_distance_rate: float):
    """
    使用opencv库中的方法读取图片，
    并将图片在水平方向平移图像大小的Horizontal_distance_rate，在垂直方向进行平移图像大小的vertical_distance_rate，
    并使用Matplotlib将转化后的图片保存在指定位置。

    Parameters
    ----------
    src_img_path：str
        原始图片的保存位置
    result_img_path: str
        转化后的图片的保存位置
    Horizontal_distance_rate：float
        水平方向平移图像大小的Horizontal_distance_rate
        Horizontal_distance_rate > 0 : 向右移动
        Horizontal_distance_rate < 0 : 向左移动
    vertical_distance_rate: float
        垂直方向进行平移图像大小的vertical_distance_rate
        vertical_distance_rate > 0 : 向下移动
        vertical_distance_rate < 0 : 向上移动

    Returns
    -------
        没有返回值
    """

    src_img = cv2.imread(src_img_path)
    # 读取有色图片,读取得到的图片格式是BGR
    src_img_RGB = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式
    rows, cols = src_img_RGB.shape[:2]
    # 获取原始图像行数和列数

    # 图像平移矩阵
    w = int(rows * Horizontal_distance_rate)
    h = int(cols * vertical_distance_rate)
    M = np.float32([[1, 0, w], [0, 1, h]])
    result_img = cv2.warpAffine(src_img_RGB, M, (cols, rows))
    # 图像平移
    plt.imshow(result_img)
    plt.axis('off')
    plt.savefig(result_img_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()


def main():
    src01_img_path = '../Photo/src_picture1_4.jpg'
    result01_img_path = '../Photo/result_picture1_4.jpg'
    Horizontal_distance_rate = -0.2
    vertical_distance_rate = 0.25
    image_panning(src01_img_path, result01_img_path, Horizontal_distance_rate, vertical_distance_rate)


if __name__ == '__main__':
    main()



