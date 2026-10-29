def fun(x, y):
    return -0.9 * y


def euler(y0, x0, x1, n):
    y = y0
    x = x0
    h = (x1 - x0) / n
    print(0, y, x)
    for i in range(1, n + 1):
        k1 = fun(x, y)
        y = y + k1 * h
        x = x + h
        print(i, k1, y, x)


def heun(y0, x0, x1, n):
    y = y0
    x = x0
    h = (x1 - x0) / n
    print(0, y, x)

    for i in range(1, n + 1):
        k1 = fun(x, y)
        k2 = fun(x + h, y + h * k1)
        y = y + (k1 + k2) * h / 2
        x = x + h
        print(i, k1, k2, y, x)


def runge_kutta4(y0, x0, x1, n):
    y = y0
    x = x0
    h = (x1 - x0) / n
    print(0, y, x)

    for i in range(1, n + 1):
        k1 = fun(x, y)
        k2 = fun(x + h / 2, y + k1 * h / 2)
        k3 = fun(x + h / 2, y + k2 * h / 2)
        k4 = fun(x + h, y + k3 * h)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        x = x + h
        print(i, k1, k2, k3, k4, y, x)


euler(0.12, 0, 1, 20)
print()
heun(0.12, 0, 1, 20)
print()
runge_kutta4(0.12, 0, 1, 20)
print()
