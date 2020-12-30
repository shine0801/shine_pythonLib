# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     gen_traindata
   Description :   生成训练数据和测试数据，生成.txt文件
   Author :       shine
   date：          2020/10/20
**********************************
"""
import os
import xml.etree.ElementTree as ET
from random import shuffle


def gen_train_data(root_path, classes, train_rate):
    """
       参数：
           root_path---VOC根目录
           classes---类别
           train_num---训练数据占比
       返回值：
           N/A
       """
    wd = os.getcwd()
    label_path = os.path.join(root_path, 'Annotations')
    image_path = os.path.join(root_path, 'JPEGImages')

    save_path = os.path.join(root_path, 'ImageSets/Main')
    f_train = open(os.path.join(save_path, 'train.txt'), 'w')
    f_test = open(os.path.join(save_path, 'test.txt'), 'w')

    # 读取标记文件和图片
    label_files = os.listdir(label_path)
    image_files = os.listdir(image_path)

    shuffle(label_files)

    train_label_list = label_files[:int(train_rate*len(label_files))]
    test_label_list = list(set(label_files) - set(train_label_list))

    # 得到训练集
    for label_name in train_label_list:
        image_name = label_name.split('.')[0]
        f_train.write(os.path.join(image_path, image_name + '.jpg'))
        f = open(os.path.join(label_path, image_name + '.xml'), 'rb')
        tree = ET.parse(f)
        root = tree.getroot()

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymax').text))
            f_train.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        f_train.write('\n')
        f.close()
    f_train.close()

    # 得到测试集
    for image_name in test_label_list:
        image_name = image_name.split('.')[0]
        f_test.write(os.path.join(image_path, image_name + '.jpg'))
        f = open(os.path.join(label_path, image_name + '.xml'))
        tree = ET.parse(f)
        root = tree.getroot()

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymax').text))
            f_test.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        f_test.write('\n')
        f.close()
    f_test.close()


if __name__ == "__main__":
    # VOC数据格式目录
    root_path = 'E:/pythonwork/yolov4/VOCdevkit/VOC2028'
    classes = ['hat', 'person']
    gen_train_data(root_path, classes, 0.9)