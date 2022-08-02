
# 在pytorch中实现将sobel算子和卷积层结合来提取图像中物体的边缘轮廓图

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#@Time : 2022/6/2 13:36
#@Author : Smile
#@File : code1_2.py
#@Software: PyCharm
@Description:
"""

import torch
import numpy as np
from matplotlib import pyplot as plt
from torch import nn
import cv2

def edge_conv2d(im):
    """
    使用卷积层对图像进行边缘轮廓提取

    Parameters
    ----------
    im
        待处理的图片

    Returns
    -------
        返回卷积后的图片
    """
    # 用nn.Conv2d定义卷积操作
    conv_op = nn.Conv2d(3, 3, kernel_size=3, padding=1, bias=False)
    # 定义sobel算子参数，所有值除以3个人觉得出来的图更好些
    sobel_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype='float32') / 3
    # 将sobel算子转换为适配卷积操作的卷积核
    sobel_kernel = sobel_kernel.reshape((1, 1, 3, 3))
    # 卷积输出通道，这里我设置为3
    sobel_kernel = np.repeat(sobel_kernel, 3, axis=1)
    # 输入图的通道，这里我设置为3
    sobel_kernel = np.repeat(sobel_kernel, 3, axis=0)
    conv_op.weight.data = torch.from_numpy(sobel_kernel)
    edge_detect = conv_op(im)
    print(torch.max(edge_detect))
    # 将输出转换为图片格式
    edge_detect = edge_detect.squeeze().detach().numpy()
    return edge_detect

def edge_extraction(src_path: str, result_path: str):
    """
    使用sobel算子和卷积层结合来提取图像中物体的边缘轮廓图

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
    im = cv2.imread(src_path, flags=1)
    im = np.transpose(im, (2, 0, 1))
    # 添加一个维度，对应于pytorch模型张量(B, N, W, H)中的batch_size
    im = im[np.newaxis, :]
    im = torch.Tensor(im)
    edge_detect = edge_conv2d(im)
    edge_detect = np.transpose(edge_detect, (1, 2, 0))
    plt.imshow(edge_detect)
    plt.axis('off')
    plt.savefig(result_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()

def main():
    src01_img_path = '../Photo/src01_picture2_2.jpg'
    result01_img_path = '../Photo/result01_picture2_2.jpg'

    src02_img_path = '../Photo/src02_picture2_2.jpg'
    result02_img_path = '../Photo/result02_picture2_2.jpg'

    edge_extraction(src01_img_path, result01_img_path)
    edge_extraction(src02_img_path, result02_img_path)


if __name__ == "__main__":
    main()



















