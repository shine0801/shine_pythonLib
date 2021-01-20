#!/usr/bin/python
"""
@author:Shine Jo
@file:mytools-PyCharm.py
@time:2020/6/2 18:34
@function: 删除两个文件夹中文件名集合集合中的差集文件
"""

import os

# 图片路径
path_1 = "E:/dataset/helmet_mask_research/src_dataset/whole_mask_face/Annotations"
# label路径
path_2 = "E:/dataset/helmet_mask_research/src_dataset/whole_mask_face/JPEGImages"

suffix_1 = '.xml'
suffix_2 = '.jpg'
num = 0
array_1 = []
array_2 = []

for item in os.listdir(path_1):
    filename = item.split('.')[0]
    array_1.append(filename)

for item in os.listdir(path_2):
    filename = item.split(".")[0]
    array_2.append(filename)


print("label数量为："+str(array_1.__len__()))
print("图片数量为："+str(array_2.__len__()))


print("----------------------------------------")
del_array_1 = list(set(array_1) - set(array_2))
print(del_array_1)
print("path1差集（应该删除多余的图片）数量为："+str(del_array_1.__len__()))

print("----------------------------------------")
del_array_2 = list(set(array_2) -set(array_1))
print(del_array_2)
print("path2反差集（应该删除多余的label）数量为："+str(del_array_2.__len__()))

print("----------------------------------------")
intersection_array = list(set(array_1).intersection(array_2))
print(intersection_array)
print("交集（应该保留）数量为："+str(intersection_array.__len__()))

"""以下操作将对磁盘文件进项删除操作，建议先备份文件或者手动删除文件"""

# 删除path_1操作
for item in del_array_1:
   del_name = item+suffix_1
   del_path = os.path.join(path_1, del_name)
   os.remove(del_path)

# 删除path_2文件
for item in del_array_2:
   del_name = item+suffix_2
   del_path = os.path.join(path_2, del_name)
   os.remove(del_path)




