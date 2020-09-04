# @Time : 2020/7/30 9:38 
# @Author : ShineJo
# @File : model.py 
# @Software: PyCharm
# @Function:

from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten,Dense
import tensorflow as tf
from tensorflow.keras.models import Model


def myModel(inputs):
    x = Flatten()(inputs)
    x = Dense(512, activation=tf.nn.relu)(x)
    output = Dense(10, activation=tf.nn.softmax)(x)

    return Model(inputs, output)
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Flatten(input_shape=(28, 28)),
    #     tf.keras.layers.Dense(512, activation=tf.nn.relu),
    #     tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    # ])