# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     test
   Description :
   Author :       shine
   date：          2020/11/12
**********************************
"""
import cv2
import os
path = "E:\pythonwork\yolov4\VOCdevkit\VOC2021\JPEGImages"

img_list = os.listdir(path)

for img_name in img_list:
    img = cv2.imread(os.path.join(path, img_name))
    if img.shape[0]<416:
        print(img_name)