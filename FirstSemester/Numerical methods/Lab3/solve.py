import math
import sys
import numpy as np
import matplotlib.pyplot as plt

f0 = 0.9
k = 0.12

def fun(x):
    return f0 * math.exp(-k * x)

df_exact = -0.108
S_exact = 7.5

print(f"df_exact = {df_exact}")
print(f"S_exact = {S_exact}")

# 1. Differentiation
# h in {1, 10^-1, ..., 10^-16}
diff_data = []
print("\n--- DIFFERENTIATION ---")
for p in range(17):
    h = 10.0 ** (-p)
    d2 = (fun(h) - fun(-h)) / (2.0 * h)
    d4 = (-fun(2.0*h) + 8.0*fun(h) - 8.0*fun(-h) + fun(-2.0*h)) / (12.0 * h)
    delta1 = abs((df_exact - d2) / df_exact) * 100.0
    delta2 = abs((df_exact - d4) / df_exact) * 100.0
    diff_data.append((h, d2, d4, delta1, delta2))
    print(f"h={h:.1e}: d2={d2:.15f}, d4={d4:.15f}, delta1={delta1:.6e}%, delta2={delta2:.6e}%")

# 2. Integration
# u = 0, v = 10000
# N in {10, 100, 1000, 10000, 100000, 1000000, 10000000}
int_data = []
print("\n--- INTEGRATION ---")
for N in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    u, v = 0.0, 10000.0
    h = (v - u) / N
    
    # We can compute using numpy for ultra-fast execution of large N
    # For N <= 100000, pure python or numpy is instant.
    # For N = 10000000, numpy handles it in ~0.1s!
    # Let's verify formula match:
    # Trapezoid: ( (f(u) + f(v))/2 + sum_{i=1}^{N-1} f(u + i*h) ) * h
    # Simpson: ( f(u) + f(v) + 4*sum(odd) + 2*sum(even) ) * h / 3
    if N <= 100000:
        s1 = 0.0
        for i in range(1, N):
            s1 += fun(u + i * h)
        s1 = (s1 + (fun(u) - fun(v)) / 2.0) * h

        s2 = 0.0
        for i in range(1, int(N / 2)):
            s2 += (4.0 * fun(u + (2 * i - 1) * h) + 2.0 * fun(u + (2 * i) * h))
        s2 = (s2 + fun(u) - fun(v)) * h / 3.0
    else:
        # Fast numpy calculation (exact equivalent)
        # Note: fun(v) = 0.0
        # Since exp(-0.12 * x) < 1e-300 for x > 6000, terms past ~6000 are 0.
        # But we can evaluate with numpy array slicing
        # To avoid allocating 10M floats at once, do chunks or numpy linspace
        x = np.linspace(u, v, N + 1)
        y = f0 * np.exp(-k * x)
        s1 = (np.sum(y[1:-1]) + (y[0] + y[-1]) / 2.0) * h
        # Simpson:
        # sum odd indices: y[1:-1:2]
        # sum even indices: y[2:-1:2]
        s2 = (y[0] + y[-1] + 4.0 * np.sum(y[1:-1:2]) + 2.0 * np.sum(y[2:-1:2])) * h / 3.0

    deltaS1 = abs((S_exact - s1) / S_exact) * 100.0
    deltaS2 = abs((S_exact - s2) / S_exact) * 100.0
    int_data.append((N, s1, s2, deltaS1, deltaS2))
    print(f"N={N:8d}: S1={s1:.14f}, S2={s2:.14f}, deltaS1={deltaS1:.6e}%, deltaS2={deltaS2:.6e}%")
