
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
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.image import imread


def Image_segmentation_based_on_KMEANS(src_path: str, result_path: str):
    """
   K-Means聚类算法是无监督学习算法，是将没有类别标签的数据集，
   把特征属性相同的数据样本集合在一起，形成一个聚类，
   其中K的取值就是聚类的个数，Means就是数据集的每一个中心点，也就是我们所说的质心

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
    X = src_img_RGB.reshape(-1, 3)
    # 处理图像数据

    # KMeans聚类
    segmented_imgs = []
    n_colors = (10, 8, 6, 4, 2)
    time_run1 = 1
    for n_cluster in n_colors:
        time_run1 = time_run1 + 1
        print(time_run1)
        kmeans = KMeans(n_clusters=n_cluster, random_state=42).fit(X)
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        segmented_imgs.append(segmented_img.reshape(src_img_RGB.shape))

    # 可视化展示
    plt.figure(1, figsize=(12, 8))
    plt.subplot(231)
    plt.imshow(src_img_RGB.astype('uint8'))
    plt.title('Original image')
    time_run2 = 1
    for idx, n_clusters in enumerate(n_colors):
        time_run2 = time_run2 + 1
        print(time_run2)
        plt.subplot(232 + idx)
        plt.imshow(segmented_imgs[idx].astype('uint8'))
        plt.title('{} colors'.format(n_clusters))

    plt.savefig(result_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()


def main():
    src01_KMEANS_path = '../Photo/src_picture4_2.jpg'
    result01_KMEANS_path = '../Photo/result_picture4_2.jpg'
    Image_segmentation_based_on_KMEANS(src01_KMEANS_path, result01_KMEANS_path)


if __name__ == '__main__':
    main()








