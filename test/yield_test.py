# @Time : 2020/8/11 9:24 
# @Author : ShineJo
# @File : yield_test.py 
# @Software: PyCharm
# @Function: 使用partial、enumerate和yield 生成数据batch
from functools import partial
import tensorflow as tf
import numpy as np


# 数据生成测试方法
def test(gen, epoch_size):
    print('进入test')

    for i, element in enumerate(gen):
        if i >= epoch_size:    # 防止无限循环
            break
        print(i, element)


# 数据生成器
def data_generator(x_data, y_data, batch_size):
    n = len(x_data)
    i = 0
    while True:
        x_list = np.zeros(shape=(0, 1))
        y_list = np.zeros(shape=(0, 1))

        for b in range(batch_size):
            x_list = np.append(x_list, x_data[i])
            y_list = np.append(y_list, y_data[i])
            i = (i + 1) % n
        yield x_list, y_list


if __name__ == "__main__":
    x_train = [1, 2, 3, 3, 4, 5, 5, 4, 1, 2]
    y_train = [1, 2, 3, 3, 4, 5, 5, 4, 1, 2]

    batch_size = 2

    epoch_size = len(x_train)//batch_size

    gen = partial(data_generator, x_data=x_train, y_data=y_train, batch_size=batch_size)

    gen = tf.data.Dataset.from_generator(gen, (tf.int64, tf.int64))

    test(gen, epoch_size)

