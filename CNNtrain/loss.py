# @Time : 2020/7/30 10:13 
# @Author : ShineJo
# @File : loss.py 
# @Software: PyCharm
# @Function:
import tensorflow as tf


def myloss(y_true, y_pred):
    loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=y_true, y_pred=y_pred)
    return loss