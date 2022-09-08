
# 获取一个指定文件夹下所有文件的完整路径

import os


def read_file(path):  # 图片的完整路径
    """从文件夹中读取数据"""
    files_list = os.listdir(path)
    file_path_list = [os.path.join(path, img) for img in files_list]
    file_path_list.sort()  # 图片路径排序
    return file_path_list

file_path01 = 'C:/YXL/lijiawen/reptile/shipingzimu/tiquzimu/Data/video/'
file_path_list = read_file(file_path01)
for i in range(len(file_path_list)):
    print(file_path_list[i])

