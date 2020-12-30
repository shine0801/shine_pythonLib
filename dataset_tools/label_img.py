#!/usr/bin/python
"""
@author:Shine Jo
@file:mytools-PyCharm.py
@time:2020/6/2 18:34
@function:打标过程中，判断xml文件和图片是否一一对应，并删除没有标签的图片
"""

import os

# 图片路径
img_path = "E:\pythonwork\yolov4\VOCdevkit\VOC2021\JPEGImages"
# label路径
label_path = "E:\pythonwork\yolov4\VOCdevkit\VOC2021\Annotations"

num = 0
label_array = []
img_array = []
for item in os.listdir(label_path):
    # label_name = item.split("_")[2]
    # label_name = label_name.split(".")[0]
    label_name=item.split('.')[0]
    label_array.append(label_name)

for img_item in os.listdir(img_path):
    # img_name = img_item.split("_")[2]
    # img_name = img_name.split(".")[0]
    img_name = img_item.split(".")[0]
    img_array.append(img_name)

print("label数量为："+str(label_array.__len__()))
print("图片数量为："+str(img_array.__len__()))


print("----------------------------------------")
del_array = list(set(img_array) -set(label_array))
print(del_array)
print("差集（应该删除多余的图片）数量为："+str(del_array.__len__()))



print("----------------------------------------")
del_array1 = list(set(label_array) -set(img_array))
print(del_array1)
print("反差集（应该删除多余的label）数量为："+str(del_array1.__len__()))



print("----------------------------------------")
intersection_array = list(set(img_array).intersection(label_array))
print(intersection_array)
print("交集（应该保留）数量为："+str(intersection_array.__len__()))

"""以下操作将对磁盘文件进项删除操作，建议先备份文件或者手动删除文件"""

# 删除图片操作
for item in del_array:
   del_img_name = "RMFD_part2_"+item+".jpg"
   del_img_path = os.path.join(img_path, del_img_name)
   os.remove(del_img_path)

# 删除label文件
for item in del_array1:
   del_label_name = item+".xml"
   del_label_path = os.path.join(label_path, del_label_name)
   os.remove(del_label_path)




