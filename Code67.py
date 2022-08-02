

########################################################################################################################

import cv2
from matplotlib import pyplot as plt


def pepper_salt_noise(src_path: str, result_path: str, threshold_value_noise=100):
    """
    给图片添加椒盐噪声
    一种图像添加椒盐噪音的方法
    椒盐噪声是一种较为常见的噪音信号，255为图像中白色噪音，称为盐噪音，0为图像中黑色噪音，称为椒噪音，当图像中同时存在两种噪音时，统称为椒盐噪音。
    在图像中添加椒盐噪声的思路：
    (1).创建一个与原图像像素相同的数组
    (2).对创建的数组用random函数进行随机赋值
    (3).赋值后将大于某一数的值置255，为白色噪音，小于某一数的值置为0.为黑色噪音，其余的区域值被赋值与原图像相同。

    Parameters
    ----------
    src_img_path：str
        原始图片的保存位置
    result_img_path: str
        转化后的图片的保存位置
    threshold_value_noise : int
        设定一个阈值，像素值大于threshold_value_noise的取255(也就是像素值大于threshold_value_noise的，全部显示白色)，
        像素值小于threshold_value_noise的小于的取0（也就是像素值小于threshold_value_noise的，全部显示黑色）

    Returns
    -------
        没有返回值
    """

    src_img = cv2.imread(src_path)
    # 读取有色图片,读取得到的图片格式是BGR
    src_img_RGB = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式
    noise = np.random.randint(0, 256, size=src_img_RGB.shape)
    # 注意这个函数是下闭上开的
    # 生成随机噪声
    threshold_value_noise = threshold_value_noise
    # 设定一个阈值，像素值大于threshold_value_noise的取255(也就是像素值大于threshold_value_noise的，全部显示白色)，
    # 像素值小于threshold_value_noise的小于的取0（也就是像素值小于threshold_value_noise的，全部显示黑色）
    noise = np.where(noise > threshold_value_noise, 255, 0)

    noise = noise.astype('float')
    pepper_salt_result = src_img_RGB.astype("float")
    # 读入的图像的数据类型是uint8，相加的话不会截取，而是自动对256取余，所以我们需要转换为float后再相加
    pepper_salt_result = pepper_salt_result + noise

    pepper_salt_result = np.where(pepper_salt_result > threshold_value_noise, 255, pepper_salt_result)
    # 这时候图像的数据都是float，并且有的是大于255的，对于大于255的，我们进行截取
    pepper_salt_result = pepper_salt_result.astype('uint8')
    plt.imshow(pepper_salt_result)
    plt.axis('off')
    plt.savefig(result_path)
    # 将转化为GRAY格式的图片保存到result_img_path位置
    plt.show()

########################################################################################################################
# 2.给图片添加高斯噪声
import cv2
import numpy as np


def gaussian_noise(src_path: str, result_path: str):
    """
    给图片添加高斯噪声
    高斯噪声，顾名思义是指服从高斯分布（正态分布）的一类噪声

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
    noise = np.random.normal(0, 30, size=src_img_RGB.shape)
    # 0 是均值，30是方差，注意这个函数是下闭上开的
    # 生成随机噪声
    gaussian_result_picture = src_img_RGB.astype("float")
    # 读入的图像的数据类型是uint8，相加的话不会截取，而是自动对256取余，所以我们需要转换为float后再相加
    gaussian_result_picture = gaussian_result_picture + noise

    gaussian_result_picture = np.where(gaussian_result_picture > 255, 255, gaussian_result_picture)
    # 这时候图像的数据都是float，并且有的是大于255的，对于大于255的，我们进行截取
    gaussian_result_picture = np.where(gaussian_result_picture < 0, 0, gaussian_result_picture)
    # 这时候图像的数据都是float，并且有的是小于0的，对于小于0的，我们进行截取
    gaussian_result_picture = gaussian_result_picture.astype('uint8')
    plt.imshow(gaussian_result_picture)
    plt.axis('off')
    plt.savefig(result_path)
    # 将转化格式的图片保存到result_path位置
    plt.show()



########################################################################################################################
def mean_filter_noise(src_path: str, result_path: str):
    """
    对图像进行均值滤波

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
    src_img_RGB = cv2.blur(src_img_RGB, (3, 3))
    # 对图像进行均值滤波处理
    # 默认为规定尺寸的1/n的全1矩阵
    src_img_RGB = src_img_RGB.astype('uint8')
    plt.imshow(src_img_RGB)
    plt.axis('off')
    plt.savefig(src_img_RGB)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()


def main():
    src_pepper_salt_path = '../Photo/src_picture3_1.jpg'
    result_pepper_salt_path = '../Photo/result_pepper_salt_picture3_1.jpg'
    pepper_salt_noise(src_pepper_salt_path, result_pepper_salt_path)

    src_gaussian__path = '../Photo/result_pepper_salt_picture3_1.jpg'
    result_gaussian_path = '../Photo/result_gaussian_picture3_1.jpg'
    gaussian_noise(src_gaussian__path, result_gaussian_path)

    src_mean_filter_path = '../Photo/result_gaussian_picture3_1.jpg'
    result_mean_filter_path = '../Photo/result_mean_filter_picture3_1.jpg'
    gaussian_noise(src_mean_filter_path, result_mean_filter_path)


if __name__ == '__main__':
    main()











