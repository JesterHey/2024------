import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 假设曲率和弧长的关系是线性的
# k(s) = k0 + k1 * s
k0 = 0.1  # 初始曲率
k1 = 0.05 # 曲率随弧长变化的速率

# 定义曲率函数
def curvature(s):
    return k0 + k1 * s

# 计算某点处的切线方向角
def tangent_angle(s):
    angle, _ = quad(curvature, 0, s)
    return angle

# 示例：计算s = 10处的切线方向角
s = 10
angle = tangent_angle(s)
print(f"The tangent angle at s = {s} is {np.degrees(angle):.2f} degrees.")

# 绘制曲线和切线方向
s_values = np.linspace(0, 20, 100)
angles = [tangent_angle(s) for s in s_values]

plt.figure(figsize=(10, 6))
plt.plot(s_values, np.degrees(angles), label='Tangent Angle (degrees)')
plt.xlabel('Arc Length (s)')
plt.ylabel('Tangent Angle (degrees)')
plt.title('Tangent Angle vs. Arc Length')
plt.legend()
plt.grid(True)
plt.show()
