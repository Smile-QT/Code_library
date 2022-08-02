
#垂直镜像翻转图像
import cv2
from matplotlib import pyplot as plt


def Vertical_image_flip_and_print(src_img_path: str, result_img_path: str):
    """
    使用opencv库中的方法读取图片，并将图片进行垂直图像翻转和打印，并使用Matplotlib将转化后
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
    # 将图片模式转化成RGB格式
    result_img = cv2.flip(result_img_RGB, 0)
    # 将图片进行垂直镜像翻转
    plt.imshow(result_img)
    plt.axis('off')
    plt.savefig(result_img_path)
    # 将垂直镜像翻转后的图片保存到result_img_path位置
    plt.show()
def main():
    src_img_path = '../Photo/src_picture1_2.jpg'
    result_img_path = '../photo/result_picture1_2.jpg'
    Vertical_image_flip_and_print(src_img_path, result_img_path)
if __name__ == '__main__':
    main()
