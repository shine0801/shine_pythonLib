# @Time : 2020/8/5 10:30 
# @Author : ShineJo
# @File : test.py 
# @Software: PyCharm
# @Function:

import cv2
import xml.etree.ElementTree as ET

def img_resize(img, max_len):
    height, width = img.shape[0], img.shape[1]
    # 设置新的图片分辨率框架
    width_new = max_len
    height_new = max_len
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        rate = width / width_new
        img_new = cv2.resize(img, (width_new, int(height * width_new / width)))
    else:
        rate = height / height_new
        img_new = cv2.resize(img, (int(width * height_new / height), height_new))
    return img_new, rate


img = cv2.imread("img/1.jpg")
# cv2.rectangle(img, (132, 117), (195, 184), (255, 0, 0), 2)
# cv2.rectangle(img, (132, 139), (195, 184), (255, 255, 0), 2)
# cv2.imshow('img', img)
img1 = img[117:184, 132:195]

img2, r = img_resize(img1, 608)
cv2.imshow('img2', img2)

cv2.waitKey(0)

