import numpy as np

#
# def f(x):
#     return 3000 - 100 * x ** 2 - 4 * x ** 5 - 6 * x ** 6
#
#
# def quadratic_approximation(f, x, h):
#     # Вычисление значений функции в точках x, x+h и x-h
#     fx = f(x)
#     fxh = f(x + h)
#     fx_minus_h = f(x - h)
#
#     # Вычисление производной функции в точке x
#     dfx = (fxh - fx_minus_h) / (2 * h)
#
#     # Вычисление квадратичной аппроксимации функции в точке x
#     a = (fx_minus_h + fxh - 2 * fx) / (h ** 2)
#     b = dfx - 2 * a * x
#     c = fx - a * x ** 2 - b * x
#
#     # Вычисление корней квадратичной аппроксимации
#     D = b ** 2 - 4 * a * c
#     if D >= 0:
#         x1 = (-b + np.sqrt(D)) / (2 * a)
#         x2 = (-b - np.sqrt(D)) / (2 * a)
#         return x1, x2
#     else:
#         return None
#
#
# # Задание начальных значений для метода
# x0 = -1.0
# h = 0.01
# tolerance = 1e-6
#
# # Применение метода квадратичной аппроксимации
# while abs(f(x0)) > tolerance:
#     approx = quadratic_approximation(f, x0, h)
#     if approx is None:
#         break
#     x1, x2 = approx
#     if abs(f(x1)) < abs(f(x2)):
#         x0 = x1
#     else:
#         x0 = x2
#
# # Вывод результата
# if abs(f(x0)) < tolerance:
#     print(f"Найденный корень: {x0}")
# else:
#     print("Не удалось найти корень")
# def f(x):
#     return 3000 - 100*x**2 - 4*x**5 - 6*x**6
#
# def bisection_method(a, b, tol):
#     roots = []
#     while abs(b - a) > tol:
#         c = (a + b) / 2
#         if f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c
#         roots.append(c)
#     return roots
#
# a = -10
# b = 10
# tol = 0.0001
# roots = bisection_method(a, b, tol)
#
# # print("Корни уравнения f = 3000 - 100*x**2 - 4*x**5 - 6*x**6 = 0:")
# # for root in roots:
# #     print(root)
#
# print(3000 - 100*2.59916776468497**2 - 4*2.59916776468497**5 - 6*2.59916776468497**6)

# def f(x):
#     return 3000 - 100*x**2 - 4*x**5 - 6*x**6
#
# def df(x):
#     return -200*x - 20*x**4 - 36*x**5
#
# def quadratic_approximation_method(x0, tol, max_iter):
#     x = x0
#     iterations = 0
#     while abs(f(x)) > tol and iterations < max_iter:
#         x_new = x - f(x) / df(x)
#         if abs(x_new - x) < tol:
#             break
#         x = x_new
#         iterations += 1
#     return x
#
# initial_guesses = np.linspace(-10, 10, 100)
# tolerance = 1e-6
# max_iterations = 100
#
# roots = []
# for guess in initial_guesses:
#     root = quadratic_approximation_method(guess, tolerance, max_iterations)
#     roots.append(root)
#
# roots = np.unique(roots)
# print("Вещественные корни уравнения f(x) = 3000 - 100*x**2 - 4*x**5 - 6*x**6:")
# for root in roots:
#     print(root)
###########################################
#Второе заданеие
# import numpy as np
# import matplotlib.pyplot as plt
#
# def f(x):
#     return 3000 - 100*x**2 - 4*x**5 - 6*x**6
#
# def quadratic_approximation_method(x0, tol, max_iter):
#     x = x0
#     roots = []
#     approximations = []
#     for i in range(max_iter):
#         fx = f(x)
#         if abs(fx) < tol:
#             roots.append(x)
#         fpx = (f(x + tol) - f(x - tol)) / (2 * tol)
#         x_new = x - fx / fpx
#         approximations.append(x_new)
#         if abs(x_new - x) < tol:
#             return roots, approximations
#         x = x_new
#     return roots, approximations
#
# # Начальное приближение и параметры метода
# #Второе приближение
# x0 = -10.0
# x01 = -10.0
# tol = 1e-6
# max_iter = 100
#
# # Применение метода квадратичной аппроксимации
# roots, approximations = quadratic_approximation_method(x0, tol, max_iter)
#
# # Вывод найденных корней
# if len(roots) > 0:
#     print("Найденные вещественные корни:")
#     for root in roots:
#         print(root)
# else:
#     print("Корни не найдены")
#
# # Построение графика процесса поиска решения
# x_values = np.linspace(-10, 10, 100)
# y_values = f(x_values)
# approximation_values = [f(x) for x in approximations]
#
# plt.figure(figsize=(8, 6))
# plt.plot(x_values, y_values, label="f(x)")
# plt.plot(approximations, approximation_values, 'ro-', label="Аппроксимации")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("График процесса поиска решения")
# plt.legend()
# plt.grid(True)
# plt.show()
###########################################
#Третье заданеие
# import numpy as np
# import matplotlib.pyplot as plt
#
# def f(x):
#     return 3000 - 100*x**2 - 4*x**5 - 6*x**6
#
# def df(x):
#     return -200*x - 20*x**4 - 36*x**5
#
# def midpoint_method(f, df, x0, tol, max_iter):
#     x = x0
#     approximations = [x]
#     for i in range(max_iter):
#         fx = f(x)
#         dfx = df(x)
#         x_new = x - fx / dfx
#         approximations.append(x_new)
#         if abs(x_new - x) < tol:
#             return x_new, approximations
#         x = x_new
#     return None, approximations
#
# # Начальное приближение и параметры метода
# x0 = 10.0
# # x0 = 10.0
# tol = 1e-6
# max_iter = 100
#
# # Применение метода средней точки
# root, approximations = midpoint_method(f, df, x0, tol, max_iter)
#
# # Вывод найденного корня
# if root is not None:
#     print("Найденный вещественный корень:", root)
# else:
#     print("Корень не найден")
#
# # Построение графика процесса решения
# x_values = np.linspace(-10, 10, 100)
# y_values = f(x_values)
# approximation_values = [f(x) for x in approximations]
#
# plt.figure(figsize=(8, 6))
# plt.plot(x_values, y_values, label="f(x)")
# plt.plot(approximations, approximation_values, 'ro-', label="Аппроксимации")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("График процесса решения")
# plt.legend()
# plt.grid(True)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3000 - 100 * x**2 - 4 * x**5 - 6 * x**6

def f_derivative(x):
    return -200 * x - 20 * x**4 - 36 * x**5

def midpoint_method(a, b, epsilon):
    midpoints = []
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        midpoints.append(c)
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return midpoints

a = -10
b = 10
epsilon = 1e-6

midpoints = midpoint_method(a, b, epsilon)

if midpoints is not None:
    print("Найденный вещественный корень:", midpoints)
else:
    print("Корень не найден")

x = np.linspace(a, b, 1000)
y = f(x)
plt.plot(x, y, label='f(x)')
plt.axhline(y=0, color='black', linestyle='--')
plt.scatter(midpoints, [0] * len(midpoints), color='red', label='Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Midpoint Method - Finding Real Roots')
plt.grid(True)
plt.show()