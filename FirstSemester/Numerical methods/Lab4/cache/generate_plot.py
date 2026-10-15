import os
import matplotlib.pyplot as plt

def generate_plot():
    A = [
        [ 1.0,  1.0,  1.0,  1.0,  1.0],
        [ 0.0,  2.1,  0.0, -0.9, -0.7],
        [-0.5, -0.9,  1.7, -0.4, -0.5],
        [ 0.0, -0.5, -0.5,  2.4, -0.3],
        [-0.2, -0.7, -0.6, -0.6,  1.8]
    ]
    B = [6.0, 0.6, -0.72, 1.32, -0.36]
    X0 = [0.0 for _ in range(5)]
    delta = 1e-10

    dimension = len(X0)
    X = X0[:]
    history = [(0, X[:])]

    for k in range(1, 40):
        for i in range(dimension):
            X[i] = B[i]
            for j in range(dimension):
                if i != j:
                    X[i] -= A[i][j] * X[j]
            X[i] /= A[i][i]

        eps = [abs(X[i] - X0[i]) for i in range(dimension)]
        ksi = [eps[i] / (abs(X[i]) + delta) for i in range(dimension)]
        X0 = X[:]
        history.append((k, X[:]))

        if max(eps) < delta and max(ksi) < delta:
            break

    # We want iterations 0 to 10 as specified in item 5.3
    sub_hist = history[:11]
    iters = [h[0] for h in sub_hist]

    x1_vals = [h[1][0] for h in sub_hist]
    x2_vals = [h[1][1] for h in sub_hist]
    x3_vals = [h[1][2] for h in sub_hist]
    x4_vals = [h[1][3] for h in sub_hist]
    x5_vals = [h[1][4] for h in sub_hist]
    exact_vals = [1.2 for _ in iters]

    plt.figure(figsize=(9.5, 5.5), dpi=300)
    
    # Modern clean styling
    plt.plot(iters, x1_vals, label='x1', marker='o', markersize=6, linewidth=1.8, color='#1f77b4')
    plt.plot(iters, x2_vals, label='x2', marker='s', markersize=6, linewidth=1.8, color='#ff7f0e')
    plt.plot(iters, x3_vals, label='x3', marker='^', markersize=6, linewidth=1.8, color='#2ca02c')
    plt.plot(iters, x4_vals, label='x4', marker='d', markersize=6, linewidth=1.8, color='#d62728')
    plt.plot(iters, x5_vals, label='x5', marker='v', markersize=6, linewidth=1.8, color='#9467bd')
    plt.plot(iters, exact_vals, label='x (точний = 1.2)', linestyle='--', linewidth=2.0, color='#333333')

    plt.title('Зміна поточного наближення розв’язку для методу Гауса — Зейделя', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('Номер ітерації (i)', fontsize=10, fontweight='bold')
    plt.ylabel('Значення наближення', fontsize=10, fontweight='bold')
    
    plt.xticks(iters)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9, loc='upper right')

    plt.tight_layout()
    out_path = os.path.join("Lab4", "plots", "gauss_seidel_convergence.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Plot saved to: {out_path}")

if __name__ == "__main__":
    generate_plot()
