# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     modify_filename
   Description :   统一修改文件夹下文件的文件名
   Author :       shine
   date：          2020/11/3
**********************************
"""
import os


def rename_filename(prefix, directory):
    """
    input:
        prefix:文件名的前缀
        directory:文件目录
    return:
        N/A
    """

    file_list = os.listdir(directory)

    for i in range(len(file_list)):
        try:
            os.rename(os.path.join(directory, file_list[i]),
                  os.path.join(directory, prefix + str(i)+'.jpg'))
        except:
            print('exception!!!')


if __name__ == "__main__":
    prefix = ''
    directory = 'E:\pythonwork\yolov4\img\mask_hat'
    rename_filename(prefix, directory)

