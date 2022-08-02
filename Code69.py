
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
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from sklearn.svm import SVC


def Image_segmentation_based_on_SVM(src_path: str, result_path: str):
    """
    实现基于SVM算法的图像分割
    使用支持向量机(SVM)实现自然图像自动分类的方法,利用区域分割方法将图像区分为前景和背景图像,
    进而提取前景图像的特征向量作为SVM训练样本,实现语义分类器。利用matlab中libsvm工具箱中，
    可以让用户利用ginput来提取背景的样本点和前景（待分割出来的目标）的样本点作为训练样本，
    而不需实现指定背景和前景的样本点，也不用额外的小软件来查看某点的RGB值，ginput即可。

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

    img_arr = np.asarray(src_img_RGB, np.float64)
    # 选取背景的关键点RGB值(10个)
    lake_RGB = np.array(
        [[189, 182, 172], [174, 160, 151], [209, 210, 205], [216, 217, 209], [228, 229, 224],
         [237, 238, 232], [230, 231, 226], [234, 235, 230], [227, 224, 219], [219, 214, 208]]
    )
    # 选取目标的关键点RGB值(10个)
    duck_RGB = np.array(
        [[69, 70, 72], [86, 89, 94], [167, 131, 115], [141, 109, 96], [164, 97, 44],
         [118, 68, 45], [168, 103, 47], [169, 103, 55], [111, 53, 49], [208, 185, 169]]
    )
    RGB_arr = np.concatenate((lake_RGB, duck_RGB), axis=0)  # 按列拼接
    # lake 用 0标记，duck用1标记
    label = np.append(np.zeros(lake_RGB.shape[0]), np.ones(duck_RGB.shape[0]))
    # 原本 img_arr 形状为(m,n,k),现在转化为(m*n,k)
    img_reshape = img_arr.reshape([img_arr.shape[0] * img_arr.shape[1], img_arr.shape[2]])
    svc = SVC(kernel='poly', degree=3)  # 使用多项式核，次数为3
    svc.fit(RGB_arr, label)  # SVM 训练样本
    predict = svc.predict(img_reshape)  # 预测测试点
    lake_bool = predict == 0.  # 为湖面的序号(bool)
    lake_bool = lake_bool[:, np.newaxis]  # 增加一列(一维变二维)
    lake_bool_3col = np.concatenate((lake_bool, lake_bool, lake_bool), axis=1)  # 变为三列
    lake_bool_3d = lake_bool_3col.reshape((img_arr.shape[0], img_arr.shape[1], img_arr.shape[2]))  # 变回三维数组(逻辑数组)
    img_arr[lake_bool_3d] = 255.  # 将湖面像素点变为白色
    img_split = Image.fromarray(img_arr.astype('uint8'))  # 数组转image
    plt.imshow(img_split)
    plt.axis('off')
    plt.savefig(result_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()


def main():
    src01_SVM_path = '../Photo/src01_picture4_1.jpg'
    result01_SVM_path = '../Photo/result01_picture4_1.jpg'
    Image_segmentation_based_on_SVM(src01_SVM_path, result01_SVM_path)

    src02_SVM_path = '../Photo/src02_picture4_1.jpg'
    result02_SVM_path = '../Photo/result02_picture4_1.jpg'
    Image_segmentation_based_on_SVM(src02_SVM_path, result02_SVM_path)


if __name__ == '__main__':
    main()





