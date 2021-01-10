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
from tqdm import tqdm
import random

path = "E:/dataset/helmet_mask_research/src_dataset/sp_mask_face/JPEGImages"

img_list = os.listdir(path)

count = 0

min_size = 500

for img in tqdm(img_list):
    img_path = os.path.join(path, img)
    image = cv2.imread(img_path)

    w, h, _ = image.shape

    if w < min_size or h < min_size:
        os.remove(img_path)









