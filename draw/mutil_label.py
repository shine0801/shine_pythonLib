# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     mutil_label
   Description :   绘制多标签
   Author :       shine
   date：          2020/12/21
**********************************
"""
from PIL import Image, ImageFont, ImageDraw
import numpy as np


def mutil_label(image, boxes, class_name, colors):
    """
    绘制矩形框以及文字
    参数：
         image---图片，PIL格式
         boxes---绘制矩形框的坐标和类别
         classes--类别文字
         colors--颜色定义
    返回值：
         N/A
    """
    # 设置字体
    font = ImageFont.truetype(font='font/simhei.ttf',
                              size=np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))

    thickness = (image.size[0] + image.size[1]) // 300

    for i in range(len(boxes)):
        # 当前框
        box = boxes[i]

        # 获取当前框的数据
        # top, left, bottom, right = box[0:4]
        left, top, right, bottom = box[0:4]
        top = top - 5
        left = left - 5
        bottom = bottom + 5
        right = right + 5
        top = max(0, np.floor(top + 0.5).astype('int32'))
        left = max(0, np.floor(left + 0.5).astype('int32'))
        bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
        right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
        class_num = box[4]

        # 获取当前框的类别与绘制的颜色
        predicted_class = class_name[class_num]
        color = colors[class_num]

        # 画框框
        label = '{}'.format(predicted_class)
        draw = ImageDraw.Draw(image)
        label_size = draw.textsize(label, font)
        label = label.encode('utf-8')

        if top - label_size[1] >= 0:
            text_origin = np.array([left, top - label_size[1]])
        else:
            text_origin = np.array([left, top + 1])

        for i in range(thickness):
            draw.rectangle(
                [left + i, top + i, right - i, bottom - i],
                outline=color)

        draw.rectangle(
            [tuple(text_origin), tuple(text_origin + label_size)],
            fill=color)
        draw.text(text_origin, str(label, 'UTF-8'), fill=(0, 0, 0), font=font)
    image.show()


if __name__ == "__main__":
    # 绘制图片的路径
    image_path = 'test.jpg'  # 960*540

    image = Image.open(image_path)

    # boxes
    boxes = [[432, 156, 476, 215, 0], [212, 99, 259, 181, 1], [633, 132, 683, 213, 2], [321, 149, 354, 182, 3]]

    # classes
    class_name = ['mask,hat', 'mask', 'hat', 'face']

    # color
    color = ['green', 'yellow', 'yellow', 'red']

    mutil_label(image, boxes, class_name, color)


