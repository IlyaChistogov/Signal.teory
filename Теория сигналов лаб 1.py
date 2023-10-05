import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x от 0 до 2π с шагом 0.01
x = np.arange(0, 2*np.pi, 0.01)

# Создаем массивы значений y для каждого значения n
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.sin(3*x)
y4 = np.sin(4*x)

# Строим графики функций
plt.plot(x, y1, label='n=1')
plt.plot(x, y2, label='n=2')
plt.plot(x, y3, label='n=3')
plt.plot(x, y4, label='n=4')

# Добавляем заголовок и метки осей
plt.title('Графики функций y = sin(nx)')
plt.xlabel('x')
plt.ylabel('y')

# Добавляем легенду
plt.legend()

# Отображаем график
plt.show()