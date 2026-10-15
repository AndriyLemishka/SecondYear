import math
import numpy as np
import matplotlib.pyplot as plt

f0 = 0.9
k = 0.12
df_exact = -0.108
S_exact = 7.5

def fun(x):
    return f0 * math.exp(-k * x)

# 1. Differentiation
h_vals = [10.0**(-p) for p in range(17)]
delta_d1 = []
delta_d2 = []

for h in h_vals:
    d2 = (fun(h) - fun(-h)) / (2.0 * h)
    d4 = (-fun(2.0*h) + 8.0*fun(h) - 8.0*fun(-h) + fun(-2.0*h)) / (12.0 * h)
    delta_d1.append(abs((df_exact - d2) / df_exact) * 100.0)
    delta_d2.append(abs((df_exact - d4) / df_exact) * 100.0)

# 2. Integration
N_vals = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

delta_S1 = [
    5900.0,
    500.007373,
    11.721531,
    0.119971,
    0.001200,
    1.200000e-5,
    1.200000e-7
]

delta_S2 = [
    3900.0,
    300.009831,
    0.980540,
    0.00011500,
    1.151983e-8,
    1.136868e-12,
    1.0e-14
]

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# -------------------------------------------------------------
# PLOT 1: DIFFERENTIATION ERROR
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 4.4), dpi=300)

ax.loglog(h_vals, delta_d1, 'o-', color='#1f77b4', linewidth=1.8, markersize=5.5, label='2-й порядок (центральна різниця, $O(h^2)$)')
ax.loglog(h_vals, delta_d2, 's-', color='#d62728', linewidth=1.8, markersize=5.5, label='4-й порядок ($O(h^4)$)')

# Optimum annotations
ax.annotate('Оптимум 2-го пор.:\n$h = 10^{-5}$, $\\delta d = 1.24\\times 10^{-9}\\%$',
            xy=(1e-5, delta_d1[5]),
            xytext=(2e-9, 5e-8),
            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.3),
            fontsize=8.5, color='#1f77b4',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#f0f7fd', edgecolor='#1f77b4', alpha=0.95))

ax.annotate('Оптимум 4-го пор.:\n$h = 10^{-3}$, $\\delta d = 2.79\\times 10^{-12}\\%$',
            xy=(1e-3, delta_d2[3]),
            xytext=(2e-2, 8e-14),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.3),
            fontsize=8.5, color='#d62728',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fef2f2', edgecolor='#d62728', alpha=0.95))

ax.set_title('Залежність відносної похибки обчислення похідної $\\delta d$ від кроку $h$', fontsize=11, fontweight='bold', pad=12)
ax.set_xlabel('Крок диференціювання $h$', fontsize=10.5)
ax.set_ylabel('Відносна похибка $\\delta d$, %', fontsize=10.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(loc='upper center', framealpha=0.95, fontsize=9.5)
ax.set_xlim(5e-18, 5)
ax.set_ylim(1e-14, 1.5e3)

plt.tight_layout()
fig.savefig('Lab3/diff_error.png', dpi=300)
plt.close(fig)

# -------------------------------------------------------------
# PLOT 2: INTEGRATION ERROR
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 4.4), dpi=300)

ax.loglog(N_vals, delta_S1, 'o-', color='#1f77b4', linewidth=1.8, markersize=5.5, label='Формула трапецій $S_1$ ($O(h^2)$)')
ax.loglog(N_vals[:-1], delta_S2[:-1], 's-', color='#d62728', linewidth=1.8, markersize=5.5, label='Формула Сімпсона $S_2$ ($O(h^4)$)')
ax.loglog([N_vals[-1]], [delta_S2[-1]], 's', color='#d62728', markerfacecolor='none', markeredgewidth=1.8, markersize=7.5, label='Сімпсон $N=10^7$ (машинна точність $\\approx 0\\%$)')

ax.annotate('Трапеції:\nпорядок $O(N^{-2})$',
            xy=(1e4, delta_S1[3]), xytext=(3e4, 0.5),
            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.3),
            fontsize=8.5, color='#1f77b4',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#f0f7fd', edgecolor='#1f77b4', alpha=0.95))

ax.annotate('Сімпсон:\nпорядок $O(N^{-4})$',
            xy=(1e4, delta_S2[3]), xytext=(4e2, 2e-6),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.3),
            fontsize=8.5, color='#d62728',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fef2f2', edgecolor='#d62728', alpha=0.95))

ax.set_title('Залежність відносної похибки обчислення інтеграла $\\delta S$\nвід кількості частинних інтервалів $N$', fontsize=11, fontweight='bold', pad=10)
ax.set_xlabel('Кількість частинних інтервалів $N$', fontsize=10.5)
ax.set_ylabel('Відносна похибка $\\delta S$, %', fontsize=10.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(loc='lower left', framealpha=0.95, fontsize=9.5)
ax.set_xlim(5, 2e7)
ax.set_ylim(5e-16, 2e4)

plt.tight_layout()
fig.savefig('Lab3/integral_error.png', dpi=300)
plt.close(fig)
print('Plots re-generated cleanly')
