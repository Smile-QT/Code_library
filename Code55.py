

# 使用opencv读取彩色图片，并将图片转化成RGB格式
import cv2
from matplotlib import pyplot as plt
def img_to_rgb(src_img_path: str, result_img_path: str):
    """
    使用opencv库中的方法读取图片，并将图片转化成RGB格式，并使用Matplotlib将转化后的图片保存
    Parameters
    ----------
    src_img_path：str
    原始图片的保存位置
    result_img_path:str
    转化后的图片的保存位置
    Returns
    2022/6/18 19:40 计算机视觉小作业
    file:///F:/google_down/计算机视觉小作业.html 2/26
    -------
    没有返回值
    """
    src_img = cv2.imread(src_img_path)
    # 读取有色图片,读取得到的图片格式是BGR
    result_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    # 将图片模式转化成RGB格式
    plt.imshow(result_img)
    plt.axis('off')
    plt.savefig(result_img_path, bbox_inches='tight', pad_inches=0.0)
    # 将转化为RGB格式的图片保存到result_img_path位置
    plt.show()
def main():
    src_img_path = '../photo/src_picture1_1.jpg'
    result_img_path = '../photo/result_picture1_1.jpg'
    img_to_rgb(src_img_path, result_img_path)
if __name__ == '__main__':
    main()
