def summa(a, n):
    result = 0
    for _ in range(0, n):
        result += a
    print(n, result)

a = 0.203
for n in range(100, 10001, 100):
    summa(a, n)
