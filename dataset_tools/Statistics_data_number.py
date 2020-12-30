# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     Statistics_data_number
   Description :   统计数据集每个类别得数量  VOC格式
   Author :       shine
   date：          2020/10/20
**********************************
"""
import os
import xml.etree.ElementTree as ET


def statistics_data_number(root_path, classes):
    """
    参数：
        root_path---VOC根目录
        classes---类别列表
    返回值：
        number---各类别列表
    """
    label_path = os.path.join(root_path, 'Annotations')
    image_path = os.path.join(root_path, 'JPEGImages')

    # 定义标记类别的数量数组
    number = [0]*len(classes)

    # 读取标记文件和图片
    label_files = os.listdir(label_path)
    image_files = os.listdir(image_path)
    print('***********************************************')
    print('共有{}张图片，{}个标记文件'.format(len(image_files), len(label_files)))
    print('***********************************************')

    # 开始读取标记文件，统计各类的数量
    for i in range(len(label_files)):
        file = open(os.path.join(label_path, label_files[i]))
        tree = ET.parse(file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            for j in range(len(classes)):
                if cls == classes[j]:
                    number[j] += 1
                    break
    return number


if __name__ == "__main__":
    # VOC数据格式目录
    root_path = 'E:/pythonwork/yolov4/VOCdevkit/VOC2028'
    # 标记的类别
    classes = ['person', 'hat']
    number = statistics_data_number(root_path, classes)
    print(0)
    # 输出各类别得数量
    for i in range(len(classes)):
        print('{}有{}个标记'.format(classes[i], number[i]))
