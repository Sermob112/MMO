import sympy

x = sympy.Symbol('x')
f = x**5 + x**4 - (x**3)/3 + 2

f_prime = sympy.diff(f, x)  # вычисляем первую производную функции
critical_points = sympy.solve(f_prime, x)  # находим критические точки решением f'(x) = 0

# Добавляем в критические точки крайние значения отрезка [-10, 10], так как на этом отрезке функция имеет экстремумы
critical_points = [-10] + critical_points + [10]

# Находим интервалы возрастания и убывания
increasing_intervals = []
decreasing_intervals = []

for i in range(len(critical_points) - 1):
    interval = (critical_points[i], critical_points[i+1])
    f_interval = sympy.simplify(f.subs(x, interval[0]) * f.subs(x, interval[1]))  # знак f(x) в интервале

    if f_interval > 0:
        if f_prime.subs(x, interval[0]) > 0:
            increasing_intervals.append(interval)
        elif f_prime.subs(x, interval[0]) < 0:
            decreasing_intervals.append(interval)
    elif f_interval == 0:
        if f_prime.subs(x, interval[0]) == 0:
            increasing_intervals.append(interval)
            decreasing_intervals.append(interval)
        elif f_prime.subs(x, interval[0]) > 0:
            increasing_intervals.append(interval)
        else:
            decreasing_intervals.append(interval)

print("Интервалы возрастания функции:")
for interval in increasing_intervals:
    print(f"{interval[0]:.2f} <= x <= {interval[1]:.2f}")

print("Интервалы убывания функции:")
for interval in decreasing_intervals:
    print(f"{interval[0]:.2f} <= x <= {interval[1]:.2f}")

# Интервалы возрастания функции:
# -10.00 <= x <= -0.92
# -0.14 <= x <= 1.46
# Интервалы убывания функции:
# -0.92 <= x <= -0.14
# 1.46 <= x <= 10.00


f_second_derivative = f.diff(x, 2)
critical_points = sympy.solvers.solveset(f_second_derivative, x, domain=sympy.S.Reals)

inflection_points = []
for point in critical_points:
    if f_second_derivative.subs(x, point) == 0:
        inflection_points.append(point)

print("Точки перегиба функции:")
for point in inflection_points:
    print(f"x = {point.evalf():.4f}")

# Точки перегиба функции:
# x = -0.3087
# x = 0.0000

intervals_of_convexity = []
intervals_of_concavity = []

critical_points = sympy.solvers.solveset(f_second_derivative, x, domain=sympy.S.Reals)

for interval in sympy.S.Reals.split():
    if interval.is_real:
        interval_f_second_derivative = f_second_derivative.subs(x, interval)
        if interval_f_second_derivative > 0:
            intervals_of_convexity.append(interval)
        elif interval_f_second_derivative < 0:
            intervals_of_concavity.append(interval)

print("Интервалы выпуклости функции:")
for interval in intervals_of_convexity:
    print(f"{interval}")

print("Интервалы вогнутости функции:")
for interval in intervals_of_concavity:
    print(f"{interval}")

# Интервалы выпуклости функции:
# (-inf, -0.308665960056922)
# (0.0, 1.16658179698267)
# Интервалы вогнутости функции:
# (-0.308665960056922, 0.0)
# (1.16658179698267, inf)
# Вычисление первой производной функции
df = sympy.diff(f, x)

# Решение уравнения df = 0 для нахождения точек локальных экстремумов
critical_points = sympy.solve(df, x)

# Вычисление знаков производной на интервалах между точками локальных экстремумов
intervals = [(-float('inf'), critical_points[0])] + \
            [(critical_points[i], critical_points[i+1]) for i in range(len(critical_points)-1)] + \
            [(critical_points[-1], float('inf'))]
signs = [sympy.sign(df.subs(x, interval[0])) for interval in intervals]

# Нахождение локальных экстремумов
local_extrema = []
for i in range(len(signs)):
    if signs[i] != 0 and signs[i] == signs[i-1]:
        x1, x2 = intervals[i]
        extrema = sympy.solve(df, x, domain=sympy.Interval(x1, x2))
        if isinstance(extrema, list):
            local_extrema.extend(extrema)
        else:
            local_extrema.append(extrema)

# Добавление концов области определения в список точек
endpoints = [-float('inf'), float('inf')]
extrema = local_extrema + endpoints

# Вычисление значений функции в найденных точках
values = [f.subs(x, point) for point in extrema]

# Определение глобальных максимумов
global_maxima = []
max_value = max(values)
for i in range(len(extrema)):
    if values[i] == max_value:
        global_maxima.append(extrema[i])

# Определение глобальных минимумов
global_minima = []
min_value = min(values)
for i in range(len(extrema)):
    if values[i] == min_value:
        global_minima.append(extrema[i])

print("Локальные максимумы: ", local_extrema)
print("Глобальные максимумы: ", global_maxima)
print("Локальные минимумы: ", local_minima)
print("Глобальные минимумы: ", global_minima)

#
# global maximum at x = -1.32218504420531, f(x) = 3.96629033859557
# global minimum at x = 0.0, f(x) = 2.0
# local maximum at x = 0.888335833592018, f(x) = 2.62076832907839
# local minimum at x = 1.20487431198954, f(x) = 1.88565786883898