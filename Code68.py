
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#@Time : 2022/6/2 13:36
#@Author : Smile
#@File : code1_2.py
#@Software: PyCharm
@Description:
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def Uniform_noise(src_path: str, result_path: str):
    """
    给图片均匀噪声

    Parameters
    ----------
    src_img_path：str
        原始图片的保存位置
    result_img_path: str
        转化后的图片的保存位置

    Returns
    -------
        没有返回值
    """

    src_img = cv2.imread(src_path)
    # 读取有色图片,读取得到的图片格式是BGR
    src_img_RGB = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式

    mean, sigma = 10, 100
    a = 2 * mean - np.sqrt(12 * sigma)  # a = -14.64
    b = 2 * mean + np.sqrt(12 * sigma)  # b = 54.64
    noiseUniform = np.random.uniform(a, b, src_img_RGB.shape)
    result_noise_Uniform_picture = src_img_RGB + noiseUniform
    result_picture3_2 = np.uint8(cv2.normalize(result_noise_Uniform_picture, None, 0, 255, cv2.NORM_MINMAX))
    # 归一化为 [0,255]
    plt.imshow(result_picture3_2)
    plt.axis('off')
    plt.savefig(result_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()


def median_filter(src_path: str, result_path: str, ksize=3):
    """
    给图片进行中值滤波

    Parameters
    ----------
    src_img_path：str
        原始图片的保存位置
    result_img_path: str
        转化后的图片的保存位置
    ksize：int
        ksize 是滤波核的大小。滤波核大小是指在滤波处理过程中其邻域图像的高度和宽度。需要注意，核大小必须是比1大的奇数，比如3、5、7等。

    Returns
    -------
        没有返回值
    """
    src_img = cv2.imread(src_path)
    # 读取有色图片,读取得到的图片格式是BGR
    src_img_RGB = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式
    result_median_filter = cv2.medianBlur(src_img_RGB, ksize)
    plt.imshow(result_median_filter)
    plt.axis('off')
    plt.savefig(result_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()


def main():
    src_Uniform_noise_path = '../Photo/src_picture3_2.jpg'
    result_Uniform_noise_path = '../Photo/result_Uniform_noise_picture3_2.jpg'
    Uniform_noise(src_Uniform_noise_path, result_Uniform_noise_path)

    src_median_filter_path = '../Photo/result_Uniform_noise_picture3_2.jpg'
    result_median_filter_path = '../Photo/result_median_filter_picture3_2.jpg'
    median_filter(src_median_filter_path, result_median_filter_path)



if __name__ == '__main__':
    main()








