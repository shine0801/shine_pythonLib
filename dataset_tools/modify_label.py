# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     update_label
   Description :   指定数据集中的标记类别，并修改此类别
   Author :       shine
   date：          2020/10/20
**********************************
"""

import os
import xml.etree.ElementTree as ET


def modify_label(root_path, res_name, modified_name):
    """
    需要的参数：
    root_path---VOC数据集的根目录
    res_name---原名称
    modified_name---修改后的名称

    返回：num---修改的数量
    """
    label_path = os.path.join(root_path, 'Annotations')
    image_path = os.path.join(root_path, 'JPEGImages')

    # 读取标记文件和图片
    label_files = os.listdir(label_path)
    image_files = os.listdir(image_path)
    num = 0

    for i in range(len(label_files)):
        file = open(os.path.join(label_path, label_files[i]), encoding='UTF-8')
        tree = ET.parse(file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls == res_name:
                obj.find('name').text = modified_name
                tree.write(os.path.join(label_path, label_files[i]))
                num += 1
    return num


if __name__ == "__main__":
    # VOC数据格式目录
    root_path = 'E:/dataset/helmet_mask_research/src_dataset/whole_mask_face'
    num = modify_label(root_path, 'face', 'mask_face')
    print('共修改{}个name'.format(num))




