# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     data_fuse
   Description :   对输出的区域进行融合
   Author :        shine
   date：          2020/11/13
**********************************
"""
from draw.draw_rectangle import draw_rectangle


def data_fuse(boxes):
    """
    input -- 输入方框 + 类别
    output -- 人脸框 （融合后的矩形）+ 类别
    """
    masks = []
    hats = []
    faces = []
    for box in boxes:
        if box[4] == 0:
            masks.append(box)
        elif box[4] == 1:
            hats.append(box)
        elif box[4] == 2:
            faces.append(box)
        else:
            print('error')
    for i in range(len(faces)):




if __name__ =="__main__":
    out_boxes = []
    out_classes = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    classes = ['mask', 'hat', 'face']
    color = ['green', 'blue', 'red']
    out_scores = [0.9996078, 0.9877851, 0.9853316, 0.9831334, 0.9414663, 0.65668654, 0.9864208, 0.9094193, 0.6681214,
                 0.9885993, 0.9870513, 0.98120826, 0.8765738, 0.7866336, 0.7684584]

    f = open('test.txt', 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        box = lines[i].strip().split(',')
        box = [round(float(c)) for c in box]
        box.append(out_classes[i])
        out_boxes.append(box)

    # draw_rectangle('test.jpg', out_boxes, classes, color)
    data_fuse(out_boxes)






