
# 读取RGB图片，并将图片转化成灰度图片
import cv2 as cv

def RGB_TO_GRAY(src_path, result_path):
    # 【读取图像】
    image = cv.imread(src_path)
    # 【将图像灰度化】
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 【显示图像】
    cv.imshow('win', image)
    cv.waitKey(0)
    cv.imwrite(result_path, image)

def main():
    src_path = 'C:\YXL\Restormer-mainV174\YXL_dir\photo01.jpg'
    result_path = 'C:\YXL\Restormer-mainV174\YXL_dir\photo005156.jpg'
    RGB_TO_GRAY(src_path, result_path)

if __name__ == '__main__':
    main()
    
