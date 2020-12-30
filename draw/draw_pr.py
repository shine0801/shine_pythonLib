# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     draw_pr
   Description :   PR曲线
   Author :       shine
   date：          2020/10/14
**********************************
"""
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

file_path = 'E:\pythonwork\yolov4\img/1/pr.csv'

reader = csv.reader(open(file_path, 'r', encoding='utf-8'))
recall = []
acc = []
for item in reader:
    recall.append(float(item[1]))
    acc.append(float(item[2]))

plt.xlabel('recall')
plt.ylabel('precision')

plt.plot(recall, acc)
plt.legend()
plt.show()





