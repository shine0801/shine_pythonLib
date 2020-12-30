# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     draw_anchor
   Description :   对Anchorbox进行处理  写入文件
   Author :       shine
   date：          2020/11/10
**********************************
"""
import cv2
import numpy as np


def draw_anchor(anchor_path):
    """
    anchor_path---存放anchor数据的txt
    """
    f = open(anchor_path, 'r')
    anchors = f.readlines()
    anchors = anchors[0].split(',')
    anchor = []
    for i in range(len(anchors)):
        if i % 2 == 1: continue
        anchor.append([int(anchors[i]), int(anchors[i + 1])])

    # 创建画布
    img = np.zeros((700, 900, 3), np.uint8)
    img[:] = [255, 255, 255]

    # 获取中心点
    x_center = int(img.shape[0] / 2)
    y_center = int(img.shape[1] / 2)

    cv2.drawKeypoints(img, (x_center, y_center), img, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    cv2.imshow('img', img)
    cv2.waitKey(0)

    return 0


if __name__ == '__main__':
    anchor_path = 'gen_anchors'
    draw_anchor(anchor_path)














