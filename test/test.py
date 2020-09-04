# @Time : 2020/7/8 10:29 
# @Author : ShineJo
# @File : test.py 
# @Software: PyCharm
# @Function:

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f_1(x, A, B):
 return A * x + B

plt.figure()
# 拟合点
x0 = [187, 167, 168, 175, 140, 150]
y0 = [83,80,67,]

# 绘制散点
plt.scatter(x0[:], y0[:], 3, "red")

# 直线拟合与绘制
A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
x1 = np.arange(30, 75, 0.01)#30和75要对应x0的两个端点，0.01为步长
y1 = A1 * x1 + B1
plt.plot(x1, y1, "blue")
print(A1)
print(B1)
plt.title(" ")
plt.xlabel('t')

plt.ylabel('Mt/g')
plt.show()
