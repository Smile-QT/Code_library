
# 对图像做快速傅里叶变换
import numpy as np
import cv2
from matplotlib import pyplot as plt


def kuaisufuliyebianhuan(src_path):
    # 1 读取图像 0表示按照灰度图片读取
    img = cv2.imread(src_path, 0)
    # 2 傅里叶变换
    # 2.1 正变换
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    # 2.2 频谱中心化
    dft_shift = np.fft.fftshift(dft)
    # 2.3 计算频谱和相位谱
    mag, angle = cv2.cartToPolar(dft_shift[:, :, 0], dft_shift[:, :, 1], angleInDegrees=True)
    mag = 20 * np.log(mag)
    # 3 图像显示
    plt.imshow(img, cmap='gray')
    plt.show()

def main():
    src_path = 'D:\YXL\Project\Paper\Restormer_run\Restormer-mainV176\YXL_dir\photo01.jpg'
    kuaisufuliyebianhuan(src_path)

if __name__ == '__main__':
    main()
