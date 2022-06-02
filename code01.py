#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#@Time : 2022/6/2 13:36
#@Author : Smile
#@File : code1_1.py
#@Software: PyCharm
@Description:
"""
# 使用opencv打开并处理图片，使用Matplotlib保存图片
import cv2
from matplotlib import pyplot as plt


def img_to_rgb(src_img_path: str, result_img_path: str):
    """
    使用opencv打开并处理图片，然后使用Matplotlib保存图片

    Parameters
    ----------
    src_img_path：str
        原始图片的保存位置
    result_img_path:str
        转化后的图片的保存位置

    Returns
    -------
        没有返回值
        :param result_img_path:
        :param src_img_path:
    """

    src_img = cv2.imread(src_img_path, cv2.IMREAD_COLOR)
    # 读取有色图片,读取得到的图片格式是BGR
    result_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式
    plt.imshow(result_img)
    plt.savefig(result_img_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()

