# @Time : 2020/7/30 9:18 
# @Author : ShineJo
# @File : test.py 
# @Software: PyCharm
# @Function:

import tensorflow as tf
from tensorflow.keras.layers import Input
from CNNtrain.model import myModel
from loss import myloss
import numpy as np
import time
from functools import partial


# 训练一个batch
@tf.function
def train_step(x_train, y_train, my_loss, net, optimizer, regularization):
    with tf.GradientTape() as tape:
        # 计算loss
        output = net(x_train, training=True)
        loss_value = my_loss(y_train, output)
        if regularization:
            # 加入正则化损失
            loss_value = tf.reduce_sum(net.losses) + loss_value
    grads = tape.gradient(loss_value, net.trainable_variables)
    optimizer.apply_gradients(zip(grads, net.trainable_variables))
    return loss_value


# 训练某一轮次
def fit_one_epoch(net, my_loss, optimizer, epoch, epoch_size, epoch_size_val, gen, gen_val, regularization=False):
    loss = 0
    val_loss = 0
    strat_time = time.time()
    for iteration, batch in enumerate(gen):
        if iteration >= epoch_size:
            break
        x_train, y_train = batch[0], batch[1]
        print(iteration, x_train)
        loss_value = train_step(x_train, y_train, my_loss, net, optimizer, regularization)
        loss = loss + loss_value


# 数据生成器
def data_generator(x, y, batch_size, input_shape):
    n = len(x)
    i = 0
    while True:
        x_data = np.zeros(shape=[0, 28, 28])
        y_data = np.zeros(shape=[0, 10])

        for b in range(batch_size):
            x_data = np.append(x_data, x[i])
            y_data = np.append(y_data, y[i])
            i = (i + 1) % n
        yield x_data, y_data


if __name__ == "__main__":

    # 数据
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    print("训练的数据：", len(x_train))
    print("验证的数据：", len(x_test))

    num_train = len(x_train)
    num_test = len(x_test)

    # 输入尺寸
    image_input = Input(shape=(28, 28))

    model_body = myModel(image_input)

    model_body.summary()

    regularization = True

    if True:
        start_epoch = 0
        end_epoch = 10
        batch_size = 10
        learning_rate_base = 1e-3

        gen = partial(data_generator, x_train, y_train, batch_size=batch_size, input_shape=image_input)
        gen = tf.data.Dataset.from_generator(gen, (tf.float32, tf.float32))
        gen = gen.shuffle(buffer_size=batch_size).prefetch(buffer_size=batch_size)

        gen_test = partial(data_generator, x_test, y_test, batch_size=batch_size)
        gen_test = tf.data.Dataset.from_generator(gen_test, (tf.float32, tf.float32))
        gen_test = gen_test.shuffle(buffer_size=batch_size).prefetch(buffer_size=batch_size)

        epoch_size = num_train//batch_size
        epoch_size_test = num_test//batch_size

        # 学习率
        lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=learning_rate_base,
            decay_steps=epoch_size,
            decay_rate=0.9,
            staircase=True
        )

        # 优化器
        optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)

        # 训练
        for epoch in range(start_epoch, end_epoch):

            # 训练某一伦次
            fit_one_epoch(model_body, myloss, optimizer, epoch, epoch_size, epoch_size_test, gen, gen_test, regularization)