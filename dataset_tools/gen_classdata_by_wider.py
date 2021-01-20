# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     gen_classdata_by_wider
   Description :   使用widerFace生成人脸分类数据集
   Author :       shine
   date：          2021/1/18
**********************************
"""
from tqdm import tqdm
import os
import cv2

gen_path = 'E:/dataset/helmet_mask_research/train_dataset/global_classification/face1'

src_path = 'E:/dataset/WIDER/WIDER_train/images/'

label_info_path = 'E:/dataset/WIDER/wider_face_split/wider_face_train_bbx_gt.txt'

f = open(label_info_path)
annos = f.readlines()

image_path = ''

# 生成的数量
min_num = 559
max_num = 6000

for anno in annos:
    anno = anno.strip('\n')
    if '.jpg' in anno:
        image_path = src_path + anno
        continue

    face_label = anno.split(' ')

    if len(face_label) == 1:
        continue

    x1 = int(face_label[0])
    y1 = int(face_label[1])
    x2 = x1 + int(face_label[2])
    y2 = y1 + int(face_label[3])

    image = cv2.imread(image_path)
    image_save = image[y1:y2, x1:x2]

    w, h, _ = image_save.shape

    if w < 40 or h < 40:
        continue

    if min_num > max_num:
        break
    cv2.imwrite(os.path.join(gen_path, 'face_'+str(min_num)+'.jpg'), image_save)
    min_num += 1




