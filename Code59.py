
# 对图像做快速傅里叶变换之后，计算两个图像在频域之间的L1loss损失(由于计算L1loss的两个图片的尺寸需要一样大，所以示例中使用的是同一张图片)
import numpy as np
import cv2
import torch
from torch import nn
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
    return mag

def main():

    src_path01 = 'D:\YXL\Project\Paper\Restormer_run\Restormer-mainV176\YXL_dir\photo01.jpg'
    mag01 = kuaisufuliyebianhuan(src_path01)

    src_path02 = 'D:\YXL\Project\Paper\Restormer_run\Restormer-mainV176\YXL_dir\photo01.jpg'
    mag02 = kuaisufuliyebianhuan(src_path02)

    loss = nn.L1Loss()
    mag01 = torch.tensor(mag01, requires_grad=True)
    mag02 = torch.tensor(mag02)
    loss_value = loss(mag01, mag02)
    print(loss_value)



if __name__ == '__main__':
    main()
