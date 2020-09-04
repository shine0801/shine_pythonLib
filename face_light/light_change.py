# @Time : 2020/8/5 11:39 
# @Author : ShineJo
# @File : light_change.py 
# @Software: PyCharm
# @Function:
import cv2
import numpy as np


img = cv2.imread("img/1.jpg")

blank = np.zeros(img.shape, img.dtype)

dst = cv2.addWeighted(img, 1, blank, 0, -100)

cv2.imshow('img', dst)

cv2.waitKey(0)

