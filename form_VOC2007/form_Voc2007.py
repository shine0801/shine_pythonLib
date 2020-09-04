# @Time : 2020/9/3 16:41
# @Author : ShineJo
# @File : test.py.py
# @Software: PyCharm
# @Function:生成VOC2007格式数据
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import os
from PIL import Image


def make_xml(xmin_tuple, ymin_tuple, xmax_tuple, ymax_tuple, clname, image_name):
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'VOC'

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = image_name

    node_object_num = SubElement(node_root, 'object_num')
    node_object_num.text = str(len(xmin_tuple))

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    im = Image.open(image_name)
    width, height = im.size
    node_width.text = str(width)

    node_height = SubElement(node_size, 'height')
    node_height.text = str(height)

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    for i in range(len(xmin_tuple)):
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = str(clname[i])
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'

        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(xmin_tuple[i])
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(ymin_tuple[i])
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(xmax_tuple[i])
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(ymax_tuple[i])

    xml = tostring(node_root, pretty_print=True)
    dom = parseString(xml)
    return dom

# xml保存的位置
save_xml_path = "Annotations/"  # 生成的.xml保存路径

# 需要存储的数据
face_mask = [[173, 78, 306, 268, 1], [278, 263, 741, 438, 1], [923, 258, 1068, 425, 0]]

# 文件名以及内容
img_nameinit = 'test.jpg'
xmin = []
ymin = []
xmax = []
ymax = []
clname = []

class_name = ['mask', 'nomask']

for i in range(0, len(face_mask)):
    xmin.append(face_mask[i][0])
    ymin.append(face_mask[i][1])
    xmax.append(face_mask[i][2])
    ymax.append(face_mask[i][3])
    if face_mask[i][4] == 1:
        clname.append('mask')
    else:
        clname.append('nomask')

dom = make_xml(xmin, ymin, xmax, ymax, clname, img_nameinit)

por = os.path.splitext(img_nameinit)
xml_name = os.path.join(save_xml_path, por[0] + '.xml')
print(xml_name)
print(dom)
with open(xml_name, 'wb') as f:
    f.write(dom.toprettyxml(indent='\t', encoding='utf-8'))

# dom = make_xml(xmin_tuple, ymin_tuple, xmax_tuple, ymax_tuple, image_name)

# xml_name = os.path.join(save_xml_path, image_name + '.xml')
# with open(xml_name, 'w') as f:
# f.write(dom.toprettyxml(indent='\t', encoding='utf-8'))
