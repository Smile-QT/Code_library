# 计算两张图片之间的PSNR和SSIM值

from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import cv2


def psnr_ssim(target_dir, prediction_dir):
    img_target = cv2.imread(target_dir)
    img_prediction = cv2.imread(prediction_dir)
    psnr_val = psnr(img_target, img_prediction)
    ssim_val = ssim(img_target, img_prediction, multichannel=True)  # 对于多通道图像(RGB、HSV等)关键词multichannel要设置为True
    return psnr_val, ssim_val

def main():
    target_dir = 'D:\YXL\Project\Paper\Restormer_run\Restormer-mainV166\Deraining\Datasets/test\Rain100H\input/1.png'
    prediction_dir = 'D:\YXL\Project\Paper\Restormer_run\Restormer-mainV166\Deraining\Datasets/test\Rain100H/target/1.png'
    psnr_val, ssim_val = psnr_ssim(target_dir, prediction_dir)
    print(psnr_val)
    print(ssim_val)

if __name__ =='__main__':
    main()

















