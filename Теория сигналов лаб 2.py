import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x от 0 до 2π с шагом 0.01
x = np.arange(0.0001, 2*np.pi, 0.01)

# Создаем массивы значений тригонометрических функций
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
y_cot = 1/np.tan(x)
y_sec = 1/np.cos(x)
y_csc = 1/np.sin(x)

# Строим графики функций
fig, axs = plt.subplots(6, 1, figsize=(8, 24))
axs[0].plot(x, y_sin)
axs[0].set_title('sin(x)')
axs[1].plot(x, y_cos)
axs[1].set_title('cos(x)')
axs[2].plot(x, y_tan)
axs[2].set_title('tan(x)')
axs[3].plot(x, y_cot)
axs[3].set_title('cot(x)')
axs[4].plot(x, y_sec)
axs[4].set_title('sec(x)')
axs[5].plot(x, y_csc)
axs[5].set_title('csc(x)')

# Добавляем метки осей
for ax in axs:
    ax.set_xlabel('x')
    ax.set_ylabel('y')

# Отображаем графики
plt.show()