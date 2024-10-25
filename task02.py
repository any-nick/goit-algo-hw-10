import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0 # Нижня межа
b = 2 # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло
def monte_carlo_integration(a, b, num_points, num_experiments):
    total_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок на інтервалі [a, b]
        x_random = np.random.uniform(a, b, num_points)
        y_random = f(x_random)

        # Обчислення площі як середнє значення функції * довжину інтервалу
        integral_value = (b - a) * np.mean(y_random)
        total_area += integral_value

    # Повертаємо середнє значення інтегралу після всіх експериментів
    return total_area / num_experiments

# Аналітичне обчислення з SciPy
def analytical_integration(a, b):
    result, error = spi.quad(f, a, b)
    return result, error


analytical_result, error = analytical_integration(a, b)
print(f"Аналітичний інтеграл: {analytical_result} ± {error}")


num_points_list = [10, 100, 1000, 5000, 10000, 15000]  # Кількість випадкових точок
num_experiments_list = [5, 20, 50, 100]  # Кількість експериментів

for num_points in num_points_list:
    for num_experiments in num_experiments_list:
        monte_carlo_result = monte_carlo_integration(a, b, num_points, num_experiments)
        print(f"Кількість точок: {num_points}, Кількість експериментів: {num_experiments}, Результат: {monte_carlo_result}")

