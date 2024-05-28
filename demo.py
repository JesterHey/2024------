import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

# 定义五次多项式曲率函数的系数
coefficients = [2.22141911, -0.08778512, 0.23123233, -0.19809915, 0.07146177, -0.00929347]

# 定义曲率函数 κ(s)
def kappa(s):
    return np.polyval(coefficients, s)

# 定义弧长范围
s_values = np.linspace(0, 10, 1000)

# 计算曲率对应的弧长
kappa_values = kappa(s_values)

# 假设曲线方程 y(x) 是由弧长参数化得到的
# 根据 ds^2 = dx^2 + dy^2, 我们可以假设 dy/dx = kappa(s) for simplicity
def ds_dx(s):
    return np.sqrt(1 + kappa(s)**2)

# 计算 x(s) 通过数值积分
x_values = cumtrapz(1/ds_dx(s_values), s_values, initial=0)

# 绘制 x-κ 图
plt.figure(figsize=(8, 4))
plt.plot(x_values, kappa_values, label='x - κ function', color='blue')
plt.xlabel('x', fontsize=14)  # 设置x轴标签的字体大小为14
plt.ylabel('κ', fontsize=14)  # 设置y轴标签的字体大小为14
plt.title('Curvature as a function of x', fontsize=16)  # 设置标题的字体大小为16
plt.legend()
plt.grid(True)

# 在每个点旁边标注其纵坐标
for i in range(0, len(x_values), 50):  # 间隔取点进行标注以避免过度拥挤
    plt.annotate(f'{kappa_values[i]:.2f}', (x_values[i], kappa_values[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
