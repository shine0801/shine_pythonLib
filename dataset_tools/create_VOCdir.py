# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     create_VOCdir
   Description :   在某个文件夹下床架VOC目录结构
   Author :       shine
   date：          2021/1/9
**********************************
"""

import os

path = 'E:/dataset/helmet_mask_research/train_dataset/region_segmentation'

if not os.path.exists(os.path.join(path, 'Annotations')):
    os.makedirs(os.path.join(path, 'Annotations'))

if not os.path.exists(os.path.join(path, 'JPEGImages')):
    os.makedirs(os.path.join(path, 'JPEGImages'))

if not os.path.exists(os.path.join(path, 'ImageSets')):
    os.makedirs(os.path.join(path, 'ImageSets'))

if not os.path.exists(os.path.join(path, 'ImageSets', 'Main')):
    os.makedirs(os.path.join(path, 'ImageSets', 'Main'))


