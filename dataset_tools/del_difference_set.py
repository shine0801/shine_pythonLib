"""
@author:Shine Jo
@file:mytools-PyCharm.py
@time:2020/6/2 18:34
@function:打标过程中，删除两个数据集的差集
"""

import os

anno_path1 = 'E:\pythonwork\yolov4\VOCdevkit\VOC2021/Annotations'
anno_path2 = 'E:\pythonwork\yolov4\VOCdevkit\VOC2021/Annotations'
img_path = 'E:\pythonwork\yolov4\VOCdevkit\VOC2021/JPEGImages'


list1 = os.listdir(anno_path1)
list2 = os.listdir(anno_path2)
list3 = os.listdir(img_path)

# 删除列表
del_list = list(set(list2) - set(list1))

for i in range(len(del_list)):

    # 删除图片的文件名
    img_name = del_list[i].split('.')[0] + '.jpg'

    # 删除路径
    del_label_path = os.path.join(anno_path2, del_list[i])
    del_img_path = os.path.join(img_path, img_name)

    # 删除操作
    os.remove(del_label_path)
    os.remove(del_img_path)
