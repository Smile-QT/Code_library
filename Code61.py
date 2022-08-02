
# 将图片逆时针旋转60度，并缩小为0.5倍
import cv2
import numpy as np
from cv2 import getRotationMatrix2D
from matplotlib import pyplot as plt
def Rotate_counterclockwise_and_shrink(src_img_path: str, result_img_path: str, counterclockwise_angle, fx_shrink, fy_shrink):
    """
    使用opencv库中的方法读取图片，
    并将图片逆时针旋转counterclockwise_angle度，
    横向缩放为原来的fx_shrink倍，纵向缩放为原来的fx_shrink倍，
    并使用Matplotlib将转化后的图片保存在指定位置。
    Parameters
    ----------
    src_img_path：str
    原始图片的保存位置
    result_img_path:str
    转化后的图片的保存位置
    Returns
    -------
    没有返回值
    """
    src_img = cv2.imread(src_img_path)
    # 读取有色图片,读取得到的图片格式是BGR
    result_img_RGB = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # # 将图片模式转化成RGB格式
    (h, w) = src_img.shape[:2]
    src_center = (w // 2, h // 2)
    M = getRotationMatrix2D(src_center, counterclockwise_angle, 1.0)
    # 得到旋转矩阵，逆时针旋转60度，尺度缩放为1，即保持原尺寸
    result_img = cv2.warpAffine(result_img_RGB, M, (w, h))
    # 得到矩阵后得用到图像的仿射变换函数才可以进行最终图像的变化
    width = int(w * fx_shrink)
    height = int(h * fy_shrink)
    result_img = cv2.resize(result_img, (width, height))
    # 将图片缩小0.5倍
    plt.imshow(result_img)
    plt.axis('off')
    plt.savefig(result_img_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()



def main():
    src_img_path = '../photo/src_picture1_3.jpg'
    result_img_path = '../photo/result_picture1_3.jpg'
    counterclockwise_angle = 60
    fx_shrink = np.float32(0.5)
    fy_shrink = np.float32(0.5)
    Rotate_counterclockwise_and_shrink(src_img_path, result_img_path, counterclockwise_angle, fx_shrink, fy_shrink)
if __name__ == '__main__':
        main()














