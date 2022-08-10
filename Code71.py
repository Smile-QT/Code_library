


# Python遍历文件夹下所有文件，并返回文件绝对地址列表

import os

def dirlist(path):  
    allfile = []
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile
