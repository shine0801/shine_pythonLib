# @Time : 2020/8/13 10:17 
# @Author : ShineJo
# @File : test.py 
# @Software: PyCharm
# @Function:
import os
import matplotlib.pyplot as plt
import numpy as np


# 获取字符串中的数字
def get_num(filename):
    tem_list = []
    new_string = ''
    for i in range(len(filename)):
        if filename[i].isnumeric() or filename[i] == '-' or filename[i] == '.':
            new_string = new_string + filename[i]
    # 44-15.0628-11.9799

    # 分开数字
    tem_list = new_string.split('-')
    return tem_list


# 排序
def my_sort(info_list):
    for i in range(len(info_list)):
        flag = False
        for j in range(len(info_list)-i-1):
            if int(info_list[j][0]) > int(info_list[j+1][0]):
                tem_list = info_list[j]
                info_list[j] = info_list[j+1]
                info_list[j+1] = tem_list
                flag = True
        if not flag:
            break
    return info_list


# 绘图
def draw_pic(info_list):
    x = np.arange(0, len(info_list))
    y1 = list(map(float, info_list[..., 1]))
    y2 = list(map(float, info_list[..., 2]))

    print(y1)
    print(y2)

    # 制作坐标轴
    my_x_ticks = np.arange(0, len(info_list), 5)
    plt.xticks(my_x_ticks)
    plt.xlabel('epoche')

    my_y_ticks = np.arange(1, 50, 4)
    plt.yticks(my_y_ticks)
    plt.ylabel('loss')

    plt.plot(x, y1, label='train_loss')
    plt.plot(x, y2, label='val_loss')

    plt.legend()
    plt.show()


file = 'weight.txt'
info_list = []
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        filename = os.path.splitext(line)[0]
        tem_list = get_num(filename)
        info_list.append(tem_list)
    # 排序
    info_list = my_sort(info_list)
    info_list = np.array(info_list)
    # 绘制
    draw_pic(info_list)
 # 绘制

