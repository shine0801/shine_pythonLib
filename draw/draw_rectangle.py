# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     draw_rectangle
   Description :   绘制结果，矩形框和文字
   Author :       shine
   date：          2020/10/21
**********************************
"""
import os
import cv2
import webcolors
from webcolors import name_to_rgb
from PIL import Image, ImageFont, ImageDraw


def rgb_bgr(r_color):
    """
    rgb和 bgr的互转
    参数：
        color---RGB或者BGR
    返回值：
        BGR或者RGB
    """
    r_color_list = list(r_color)
    tmp = r_color_list[0]
    r_color_list[0] = r_color_list[2]
    r_color_list[2] = tmp
    r_color = webcolors.IntegerRGB(r_color_list[0], r_color_list[1], r_color_list[2])
    return r_color


def get_r_width(box):
    """
    获取矩形框的自适应宽度
    参数：
        box---要绘制的矩形框-list
    返回值：
        width---矩形框的宽度-int
    """
    w = box[2] - box[0]
    h = box[3] - box[1]
    width = w if w < h else h
    width = int(0.05*width)
    return width


# 使用opencv-python
def draw_rectangle_cv2(image, boxes, classes, colors):
    """
    绘制矩形框以及文字
    参数：
         img_path---图片的路径
         boxes---绘制矩形框的坐标和类别
         classes--类别文字
         colors--颜色定义
    返回值：
         N/A
    """

    for i in range(len(boxes)):
        x1 = boxes[i][0]
        y1 = boxes[i][1]
        x2 = boxes[i][2]
        y2 = boxes[i][3]
        # 矩形框的颜色
        r_color = name_to_rgb(colors[boxes[i][4]])
        r_color = rgb_bgr(r_color)

        # 矩形框的宽度
        width = get_r_width(boxes[i])

        # 绘制矩形框
        cv2.rectangle(image,
                      (x1, y1),
                      (x2, y2),
                      r_color,
                      width)

        # 绘制文字的矩形框

        # y3 = int(y1 + (y2 - y1) * 0.15)
        # cv2.rectangle(image,
        #               (x1, y1),
        #               (x2, y3),
        #               r_color,
        #               -1)

        # 绘制文字
        # r_class = classes[boxes[i][4]]
        # cv2.putText(image,
        #             r_class,
        #             (x1, y3),
        #             cv2.QT_FONT_NORMAL,
        #             (x2-x1)*0.009,
        #             (255, 255, 255),
        #
        #             )

    cv2.imshow('img', image)
    cv2.waitKey(0)


# 使用PIL绘制
def draw_rectangle_pil(image, boxes, classes, colors):
    """
        绘制矩形框以及文字
        参数：
             image---图片的路径(PIL)
             boxes---绘制矩形框的坐标和类别
             classes--类别文字
             colors--颜色定义
        返回值：
             N/A
        """

    draw = ImageDraw.Draw(image)

    for i in range(len(boxes)):
        x1 = boxes[i][0]
        y1 = boxes[i][1]
        x2 = boxes[i][2]
        y2 = boxes[i][3]

        # 矩形框的宽度
        width = get_r_width(boxes[i])
        r_color = colors[boxes[i][4]]

        draw.rectangle((x1, y1, x2, y2),
                       fill=None,
                       outline=r_color,
                       width=width
                       )
    image.show()


if __name__ == "__main__":

    # 绘制图片的路径
    image_path = 'E:/dataset/WIDER/WIDER_train/images/0--Parade/0_Parade_marchingband_1_446.jpg'  # 960*540

    # boxes
    # boxes = [[432, 156, 476, 215, 0], [212, 99, 259, 181, 1], [633, 132, 683, 213, 2], [321, 149, 354, 182, 3]]
    boxes = [[628, 69, 151+628, 182+69, 0], [414, 171, 129+414, 174+171, 1], [206, 120, 126+206, 18+120, 2], [246, 14, 35+246, 41+14, 3]]

    # classes
    classes = ['mask_hat', 'mask', 'hat', 'face']

    # color
    color = ['green', 'red', 'red', 'red']

    # image = cv2.imread(image_path)
    #
    # # draw
    # draw_rectangle_cv2(image, boxes, classes, color)

    image = Image.open(image_path)
    draw_rectangle_pil(image, boxes, classes, color)









