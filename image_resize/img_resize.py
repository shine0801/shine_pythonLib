# @Time : 2020/7/3 20:16 
# @Author : ShineJo
# @File : img_resize.py 
# @Software: PyCharm
# @Function: 等比例放缩图片

import cv2

"""等比例放缩图片，返回放缩后的图片和放缩比例"""


def img_resize(img, max_len):
    height, width = img.shape[0], img.shape[1]
    # 设置新的图片分辨率框架
    width_new = max_len
    height_new = max_len
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        rate = width / width_new
        img_new = cv2.resize(img, (width_new, int(height * width_new / width)))
    else:
        rate = height / height_new
        img_new = cv2.resize(img, (int(width * height_new / height), height_new))
    return img_new, rate


if __name__ == '__main__':
    img_path = "../draw/cat.jpg"
    image = cv2.imread(img_path)
    print(image.shape)
    resized_img, r = img_resize(image, 100)
    print(resized_img.shape)
    cv2.imshow("img", resized_img)
    cv2.waitKey(0)






