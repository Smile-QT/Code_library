
# 用基于阈值的方法实现图像边缘轮廓提取

# 因为基于阈值的轮廓提取是针对灰色图片的，所以需要先将彩色图片转化成灰色图像
from PIL import Image
import cv2
from matplotlib import pyplot as plt
def Threshold_based_contour_extraction(src_img_path: str, result_img_path: str, maxValue=255, 
                                              adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                              thresholdType=cv2.THRESH_BINARY_INV, blockSize=3, C=5):
    """
    使用opencv库中的方法读取图片，
    基于阈值对图片进行轮廓提取
    (只有灰色图像才能进行基于阈值进行轮廓提取，所以首先需要将传入的图片转化成灰色图片)
    (这个函数大致意思就是把图片每个像素点作为中心取N*N的区域，然后计算这个区域的阈值，来决定
    并使用Matplotlib将转化后的图片保存在指定位置。
    Parameters
    ----------
    src_img_path：str
    原始图片的保存位置
    result_img_path: str
    转化后的图片的保存位置
    maxValue：int
    满足条件的像素点需要设置的灰度值。（将要设置的灰度值）
    Returns
    -------
    没有返回值
    """
    src_img = cv2.imread(src_img_path)
    # 读取有色图片,读取得到的图片格式是BGR
    src_img_RGB = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式
    src_img_GRAY = cv2.cvtColor(src_img_RGB, cv2.COLOR_RGB2GRAY)
    # 将图片模式转化成GRAY格式
    result_picture2_1 = cv2.adaptiveThreshold(src_img_GRAY, maxValue, adaptiveMethod, thresholdType, blockSize, C)
    # 这个函数大致意思就是把图片每个像素点作为中心取N*N的区域，然后计算这个区域的阈值，来决定
    # 基于阈值对图片进行轮廓提取
    plt.imshow(result_picture2_1, cmap='Greys_r')
    plt.axis('off')
    plt.savefig(result_img_path)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()
def main():
    src01_img_path = '../Photo/src01_picture2_1.jpg'
    result01_img_path = '../Photo/result01_picture2_1.jpg'
    src02_img_path = '../Photo/src02_picture2_1.jpg'
    result02_img_path = '../Photo/result02_picture2_1.jpg'
    maxValue = 5
    Threshold_based_contour_extraction(src01_img_path, result01_img_path, maxValue)
    Threshold_based_contour_extraction(src02_img_path, result02_img_path, maxValue)
if __name__ == '__main__':
    main()  
























