import math

def dirivative(x, h):
    d2 = (fun(x + h) - fun(x - h)) / (2 * h)
    d4 = (-fun(x + 2*h) + 8 * fun(x + h) - 8 * fun(x - h) + fun(x - 2*h)) / (12*h)
    print(h, d2, d4)


def integral(u, v, n):
    s1 = 0
    s2 = 0
    h = (v - u) / n

    for i in range(1, n):
        s1 = s1 + fun(u + i * h)
    s1 = (s1 + (fun(u) - fun(v)) / 2) * h

    for i in range(1, int(n / 2)):
        s2 = s2 + (4 * fun(u + (2 * i - 1) * h) + 2.0 * fun(u + (2 * i) * h))
    s2 = (s2 + fun(u) - fun(v)) * h / 3
    
    print(n, s1, s2)


def fun(x):
    return 0.9 * math.exp(-0.12 * x)


dirivative(0, 1)
dirivative(0, 0.1)
dirivative(0, 0.01)
dirivative(0, 0.001)
dirivative(0, 0.0001)
dirivative(0, 0.00001)
dirivative(0, 0.000001)
dirivative(0, 0.0000001)
dirivative(0, 0.00000001)
dirivative(0, 0.000000001)
dirivative(0, 0.0000000001)
dirivative(0, 0.00000000001)
dirivative(0, 0.000000000001)
dirivative(0, 0.0000000000001)
dirivative(0, 0.00000000000001)
dirivative(0, 0.000000000000001)
dirivative(0, 0.0000000000000001)

print()

integral(0, 10000, 10)
integral(0, 10000, 100)
integral(0, 10000, 1000)
integral(0, 10000, 10000)
integral(0, 10000, 100000)
integral(0, 10000, 1000000)
integral(0, 10000, 10000000)
