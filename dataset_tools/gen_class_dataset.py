# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     gen_class_dataset
   Description :   生成分类的数据集(截取部分图像用于分类)
   Author :       shine
   date：          2020/12/1
**********************************
"""
import os
import xml.etree.ElementTree as ET
from random import shuffle
import cv2
import time
from tqdm import tqdm

if __name__ == "__main__":

    # VOC格式的根目录
    root_path = 'E:/dataset/helmet_mask_research/src_dataset/whole_mask_face'

    # 分类图片的保存目录
    save_path = 'E:/dataset/helmet_mask_research/train_dataset/global_classification'

    # 保存的文件名前缀（.xml文件中的name）
    prefix_name = 'face'
    count = 0
    # 创建文件夹
    if not os.path.exists(os.path.join(save_path, prefix_name)):
        os.makedirs(os.path.join(save_path, prefix_name))

    label_list = os.listdir(os.path.join(root_path, 'Annotations'))
    img_list = os.listdir(os.path.join(root_path, 'JPEGImages'))

    for img in tqdm(img_list):
        # 读取图片
        image = cv2.imread(os.path.join(root_path, 'JPEGImages', img))

        # 获取xml中的box
        img_name = img.split('.')[0]
        f = open(os.path.join(root_path, 'Annotations', img_name + ".xml"))
        tree = ET.parse(f)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls == prefix_name:
                xmlbox = obj.find('bndbox')
                b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                     int(xmlbox.find('ymax').text))
                image_save = image[b[1]:b[3], b[0]:b[2]]
                count = count + 1
                try:
                    cv2.imwrite(os.path.join(save_path, prefix_name, img_name + '_' + str(count) + '.jpg'), image_save)
                except:
                    print(img_name)
    print(count)







