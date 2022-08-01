
# 计算两张图片之间的L1loss
import numpy as np
from PIL import Image

def L1(pred, target):
    loss = np.mean(np.abs(pred - target))
    return loss

def main():
    src_path01 = 'C:\YXL\Restormer-mainV174\YXL_dir\photo01.jpg'
    src_path02 = 'C:\YXL\Restormer-mainV174\YXL_dir\photo02.jpg'

    imgA = Image.open(src_path01)
    pred = np.array(imgA)

    imgB = Image.open(src_path02)
    target = np.array(imgB)

    L1loss_value = L1(pred, target)
    print(L1loss_value)

if __name__ == "__main__":
    main()











