# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     gen_traindata
   Description :   生成最终训练数据或者测试，生成.txt文件
   Author :       shine
   date：          2020/10/20
**********************************
"""
import os
import xml.etree.ElementTree as ET
from random import shuffle


def gen_train_data(root_path, filename , classes):
    """
       参数：
           root_path---VOC根目录
           filename ----- 生成的文件名 ---测试集还是训练集
           classes---类别

       返回值：
           N/A
        生成文件：
        在root_path下生成 filename
       """
    # 训练集或者测试集的.txt(只包括文件名，连后缀都不包括)
    label_info_path = os.path.join(root_path, 'ImageSets/Main/' + filename)

    # .xml文件的存放目录
    label_path = os.path.join(root_path, 'Annotations/')
    image_path = os.path.join(root_path, 'JPEGImages/')

    # 保存生成的文件位置
    save_path = os.path.join(root_path, filename)

    f_info = open(label_info_path)
    f_save = open(save_path, 'w')

    label_list = f_info.readlines()

    print(label_list)

    # 生成数据
    for label_name in label_list:

        # 去掉\n字符

        label_name = label_name.replace('\n', '')

        # 写入图片的路径
        f_save.write(os.path.join(image_path, label_name + '.jpg'))

        # 打开.xml文件
        f = open(os.path.join(label_path, label_name + '.xml'), 'rb')
        tree = ET.parse(f)
        root = tree.getroot()

        for obj in root.iter('object'):
            cls = obj.find('name').text
            try:
               cls_id = classes.index(cls)
            except:
                print(label_name)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymax').text))
            f_save.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        f_save.write('\n')
        f.close()

    # 关闭两个txt文件
    f_info.close()
    f_save.close()


if __name__ == "__main__":
    # VOC数据格式目录
    root_path = 'E:/dataset/helmet_mask_research/src_dataset/whole_helmet_face'

    # 测试集还是训练集
    filename = 'helmet_test.txt'

    # 数据中的类别
    classes = ['face', 'helmet_face', 'mask_face']

    gen_train_data(root_path, filename, classes)