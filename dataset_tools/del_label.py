# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     del_label
   Description :   删除数据xml文件中某个固定标签
   Author :       shine
   date：          2021/1/8
**********************************
"""
import os
import xml.etree.ElementTree as ET


def del_laebl(src_path, label_name):
    """
    src_path -----VOC根目录
    label_name ---- 要输出的标签信息

    num ---返回删除的数量
    """
    num = 0
    label_path = os.path.join(src_path, 'Annotations')

    # 读取标记文件
    label_files = os.listdir(label_path)

    for i in range(len(label_files)):
        file = open(os.path.join(label_path, label_files[i]), encoding='UTF-8')
        tree = ET.parse(file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls == label_name:
                root.remove(obj)
                tree.write(os.path.join(label_path, label_files[i]))
                num += 1
    return num


if __name__ == "__main__":
    # VOC数据格式目录
    src_path = "E:/dataset/helmet_mask_research/src_dataset/whole_helmel_face"
    label_name = "helmet"
    num = del_laebl(src_path, label_name)
    print('共删除{}个{}'.format(num, label_name))
