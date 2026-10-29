import os
import math
import matplotlib.pyplot as plt

def generate_plots():
    os.makedirs("Lab6/plots", exist_ok=True)
    
    y0 = 0.12
    x0 = 0.0
    x1 = 1.0
    n = 20
    h = (x1 - x0) / n
    
    def fun(x, y):
        return -0.9 * y
        
    def analytical(x):
        return 0.12 * math.exp(-0.9 * x)

    # 1. Compute solutions
    x_vals = [x0 + i * h for i in range(n + 1)]
    y_exact = [analytical(x) for x in x_vals]
    
    # Euler
    y_euler = [y0]
    y_cur = y0
    x_cur = x0
    for i in range(1, n + 1):
        k1 = fun(x_cur, y_cur)
        y_cur = y_cur + k1 * h
        x_cur = x_cur + h
        y_euler.append(y_cur)
        
    # Heun
    y_heun = [y0]
    y_cur = y0
    x_cur = x0
    for i in range(1, n + 1):
        k1 = fun(x_cur, y_cur)
        k2 = fun(x_cur + h, y_cur + h * k1)
        y_cur = y_cur + (k1 + k2) * h / 2
        x_cur = x_cur + h
        y_heun.append(y_cur)
        
    # RK4
    y_rk4 = [y0]
    y_cur = y0
    x_cur = x0
    for i in range(1, n + 1):
        k1 = fun(x_cur, y_cur)
        k2 = fun(x_cur + h / 2, y_cur + k1 * h / 2)
        k3 = fun(x_cur + h / 2, y_cur + k2 * h / 2)
        k4 = fun(x_cur + h, y_cur + k3 * h)
        y_cur = y_cur + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        x_cur = x_cur + h
        y_rk4.append(y_cur)
        
    # Errors
    delta_euler = [abs(y_exact[i] - y_euler[i]) for i in range(n + 1)]
    delta_heun = [abs(y_exact[i] - y_heun[i]) for i in range(n + 1)]
    delta_rk4 = [abs(y_exact[i] - y_rk4[i]) for i in range(n + 1)]
    
    # Plot 1: Function Comparison
    plt.figure(figsize=(9.5, 5.8), dpi=300)
    
    # High resolution curve for analytical solution
    dense_x = [i / 200.0 for i in range(201)]
    dense_y = [analytical(x) for x in dense_x]
    
    plt.plot(dense_x, dense_y, label='Аналітичний розв’язок y(x) = 0.12·exp(–0.9x)', color='#2b2b2b', linewidth=2.4, linestyle='-')
    plt.plot(x_vals, y_euler, label='Метод Ейлера (y1)', marker='o', markersize=5.5, linewidth=1.6, color='#d9534f', linestyle='--')
    plt.plot(x_vals, y_heun, label='Метод Гюна (y2)', marker='s', markersize=5.0, linewidth=1.6, color='#f0ad4e', linestyle='-.')
    plt.plot(x_vals, y_rk4, label='Метод Рунге – Кутта (y4)', marker='^', markersize=5.0, linewidth=1.6, color='#0275d8', linestyle=':')
    
    plt.title('Графік функції y(x): порівняння аналітичного та чисельних методів', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('x', fontsize=11, fontweight='bold')
    plt.ylabel('y', fontsize=11, fontweight='bold')
    plt.xticks([round(x, 2) for x in x_vals[::2]])
    plt.xlim(-0.02, 1.02)
    plt.grid(True, linestyle=':', alpha=0.65)
    plt.legend(frameon=True, facecolor='white', framealpha=0.95, fontsize=10, loc='upper right')
    plt.tight_layout()
    
    plot1_path = os.path.join("Lab6", "plots", "function_comparison_plot.png")
    plt.savefig(plot1_path, dpi=300)
    plt.close()
    print(f"Function plot saved to: {plot1_path}")
    
    # Plot 2: Absolute Error Comparison (Logarithmic Y Scale)
    plt.figure(figsize=(9.5, 5.8), dpi=300)
    
    # Ignore index 0 (delta = 0) for log scale or plot from i = 1
    plot_x = x_vals[1:]
    plot_delta_euler = delta_euler[1:]
    plot_delta_heun = delta_heun[1:]
    plot_delta_rk4 = delta_rk4[1:]
    
    plt.semilogy(plot_x, plot_delta_euler, label='Похибка методу Ейлера (Δ1)', marker='o', markersize=6, linewidth=1.8, color='#d9534f')
    plt.semilogy(plot_x, plot_delta_heun, label='Похибка методу Гюна (Δ2)', marker='s', markersize=6, linewidth=1.8, color='#f0ad4e')
    plt.semilogy(plot_x, plot_delta_rk4, label='Похибка методу Рунге – Кутта (Δ4)', marker='^', markersize=6, linewidth=1.8, color='#0275d8')
    
    plt.title('Графік абсолютної похибки обчислення Δ (логарифмічна шкала)', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('x', fontsize=11, fontweight='bold')
    plt.ylabel('Абсолютна похибка Δ = |y - y_num| (log scale)', fontsize=11, fontweight='bold')
    plt.xticks([round(x, 2) for x in plot_x[::2]])
    plt.xlim(0.03, 1.02)
    plt.grid(True, which='both', linestyle=':', alpha=0.65)
    plt.legend(frameon=True, facecolor='white', framealpha=0.95, fontsize=10, loc='center right')
    plt.tight_layout()
    
    plot2_path = os.path.join("Lab6", "plots", "error_comparison_plot.png")
    plt.savefig(plot2_path, dpi=300)
    plt.close()
    print(f"Error plot saved to: {plot2_path}")

if __name__ == "__main__":
    generate_plots()
