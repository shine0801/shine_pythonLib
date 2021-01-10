# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     sp_train_test
   Description :  分离测试数据和训练数据
   Author :       shine
   date：          2021/1/10
**********************************
"""
import os
import random


def sp_train_test(root_path, rate):
    """
    需要的参数：
    root_path :VOC格式的根目录
    rate = 训练集占有的比例

    生成路径root_path/ImageSets/Main/train.txt
                                    test.txt
    """

    file_list = os.listdir(os.path.join(root_path, 'JPEGImages'))

    random.shuffle(file_list)

    train_num = int(len(file_list) * rate)
    test_num = len(file_list) - train_num

    train_file = open(os.path.join(root_path, 'ImageSets/Main/train.txt'), 'w')
    test_file = open(os.path.join(root_path, 'ImageSets/Main/test.txt'), 'w')

    # 写入训练集
    for file in file_list[0: train_num]:
        name = file.split('.')[0]
        train_file.write(name)
        train_file.write('\n')

    # 写入测试集
    for file in file_list[train_num:]:
        name = file.split('.')[0]
        test_file.write(name)
        test_file.write('\n')


if __name__ == "__main__":
    # VOC数据格式目录
    root_path = 'E:/dataset/helmet_mask_research/src_dataset/sp_mask_face'
    sp_train_test(root_path, 0.8)