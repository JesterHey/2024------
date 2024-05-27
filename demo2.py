from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from demo import p
# 定义多项式函数
def poly_func(x):
    return p[0] * x**3 + p[1] * x**2 + p[2] * x + p[3]

# 生成数据点
x_vals = np.linspace(0,3,100)
y_vals = poly_func(x_vals)

# 创建插值函数
inv_func = interp1d(y_vals, x_vals, kind='linear', fill_value="extrapolate") # 

# 使用插值函数计算反函数值
inv_y_vals = np.linspace(np.min(y_vals), np.max(y_vals), 400)
inv_x_vals = inv_func(inv_y_vals)

# 绘制原函数和反函数
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='y = poly_func(x)')
plt.plot(inv_x_vals, inv_y_vals, label='x = inverse_func(y)', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Function and Its Inverse (Interpolation)')
plt.legend()
plt.grid(True)
plt.show()
