# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     gen_class_dataset
   Description :   生成分类的数据集
   Author :       shine
   date：          2020/12/1
**********************************
"""
import os
import xml.etree.ElementTree as ET
from random import shuffle
import cv2

if __name__ == "__main__":

    root_path = 'E:/pythonwork/yolov4/VOCdevkit/VOC2028'
    txt_path = os.path.join(root_path, 'ImageSets/Main/train.txt')

    # 分类图片的目录
    class_dir = os.path.join(root_path, 'classify_dir')

    # 文件名前缀
    prefix_name = ['hat', 'face']
    class_num = [0, 0]

    f = open(txt_path, 'r')
    annotations = f.readlines()
    for lines in annotations:
        anno_list = lines.split(' ')
        image = cv2.imread(anno_list[0])
        for data in anno_list[1:]:
            data = data.split(',')
            image_x = image[int(data[1]):int(data[3]), int(data[0]):int(data[2])]

            if class_num[0] <= 500 and int(data[4]) == 0 and image_x.shape[0] > 200 and image_x.shape[1] > 200:
                class_num[0] = class_num[0] + 1
                cv2.imwrite(os.path.join(class_dir, prefix_name[0]+'_'+str(class_num[0])+'.jpg'), image_x)

            if class_num[1] <= 500 and int(data[4]) == 1 and image_x.shape[0] > 200 and image_x.shape[1] > 200:
                class_num[1] = class_num[1] + 1
                cv2.imwrite(os.path.join(class_dir, prefix_name[1]+'_'+str(class_num[1])+'.jpg'), image_x)






