import sympy as sp

# Определение переменной x
x = sp.Symbol('x')

# Определение функции f(x)
f = 3000 - 100*x**2 - 4*x**5 - 6*x**6

# Определение производной функции f(x)
df = sp.diff(f, x)

# Определение функций f(x) и df(x) в виде лямбда-функций
f_lambda = sp.lambdify(x, f)
df_lambda = sp.lambdify(x, df)

def newton_method(f, df, x0, tol):
    """
    Реализация метода Ньютона для решения уравнения f(x) = 0.

    Аргументы:
    f -- функция, корень которой требуется найти
    df -- производная функции f
    x0 -- начальное приближение
    tol -- заданная точность

    Возвращает найденный корень x.
    """
    x = x0
    while True:
        fx = f_lambda(x)
        dfx = df_lambda(x)
        x_new = x - fx/dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new

# Начальное приближение
x0 = 0.5

# Заданная точность
tol = 1e-6

# Вычисление корня уравнения f(x) = 0 методом Ньютона
root = newton_method(f_lambda, df_lambda, x0, tol)

print(f'Корень уравнения f(x) = 3000 - 100*x^2 - 4*x^5 - 6*x^6 = 0: {root}')