
def quadratic_approximation(f, x0, h, eps):
    x = x0
    fx = f(x)
    while abs(fx) > eps:
        f1 = (f(x+h) - f(x))/h
        f2 = (f(x+h) - 2*fx + f(x-h))/h**2
        x = x - fx/(f1 + 0.5*f2*fx)
        fx = f(x)
    return x
def f(x):
    return 3000 - 100*x**2 - 4*x**5 - 6*x**6
root1 = quadratic_approximation(f, -1, 0.001, 0.0001)
print(root1)
root2 = quadratic_approximation(f, 0, 0.001, 0.0001)
print(root2)
root3 = quadratic_approximation(f, 1, 0.001, 0.0001)
print(root2)