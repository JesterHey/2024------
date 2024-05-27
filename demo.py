import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

# 定义弧长-曲率关系
def kappa(s):
    return np.sin(s)

# 定义初始条件
theta0 = 0  # 初始角度
x0, y0 = 0, 0  # 初始点

# 定义弧长范围
s = np.linspace(0, 10, 1000)

# 计算切线角度 theta(s)
theta = cumtrapz(kappa(s), s, initial=0) + theta0

# 计算参数方程 x(s) 和 y(s)
x = x0 + cumtrapz(np.cos(theta), s, initial=0)
y = y0 + cumtrapz(np.sin(theta), s, initial=0)

# 绘制曲线
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Reconstructed Curve from Curvature')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Reconstructed Curve from Arc Length-Curvature Relationship')
plt.legend()
plt.grid(True)
plt.show()
