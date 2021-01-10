# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     merge_files
   Description :   合并两个文件的内容
   Author :       shine
   date：          2021/1/10
**********************************
"""

import os


def merge_file(path1, path2, path3):
    """
    path1  --- 合并前的路径
    path2  --- 合并前的路径
    path3  --- 合并后的路径
    """
    f1 = open(path1)
    f2 = open(path2)
    f3 = open(path3, 'w')

    list1 = f1.readlines()
    list2 = f2.readlines()

    for info in list1:
        f3.write(info)

    for info in list2:
        f3.write(info)


if __name__ == "__main__":

    filename = 'test.txt'
    path1 = 'E:/dataset/helmet_mask_research/src_dataset/sp_helmet_face/ImageSets/Main/' + filename
    path2 = 'E:/dataset/helmet_mask_research/src_dataset/sp_mask_face/ImageSets/Main/' + filename
    path3 = 'E:/dataset/helmet_mask_research/train_dataset/region_segmentation/ImageSets/Main/' + filename
    merge_file(path1, path2, path3)





