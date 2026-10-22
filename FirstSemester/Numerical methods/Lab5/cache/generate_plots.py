import os
import matplotlib.pyplot as plt

def generate_plots():
    os.makedirs("Lab5/plots", exist_ok=True)
    
    # 1. Bisection Data (i = 0 to 10 as required by item 5.3)
    bisection_data = [
        (0, 0.0, 0.35, 0.175),
        (1, 0.0, 0.175, 0.0875),
        (2, 0.0875, 0.175, 0.13125),
        (3, 0.0875, 0.13125, 0.109375),
        (4, 0.109375, 0.13125, 0.1203125),
        (5, 0.109375, 0.1203125, 0.11484375),
        (6, 0.11484375, 0.1203125, 0.117578125),
        (7, 0.117578125, 0.1203125, 0.1189453125),
        (8, 0.1189453125, 0.1203125, 0.11962890625),
        (9, 0.11962890625, 0.1203125, 0.119970703125),
        (10, 0.119970703125, 0.1203125, 0.1201416015625)
    ]
    
    iters_bis = [d[0] for d in bisection_data]
    a_vals = [d[1] for d in bisection_data]
    b_vals = [d[2] for d in bisection_data]
    c_vals = [d[3] for d in bisection_data]
    x2_bis = [0.12 for _ in iters_bis]
    
    plt.figure(figsize=(9.5, 5.5), dpi=300)
    plt.plot(iters_bis, a_vals, label='a (ліва межа)', marker='o', markersize=6, linewidth=1.8, color='#1f77b4')
    plt.plot(iters_bis, b_vals, label='b (права межа)', marker='s', markersize=6, linewidth=1.8, color='#d62728')
    plt.plot(iters_bis, c_vals, label='c (середина / поточне наближення)', marker='^', markersize=6, linewidth=1.8, color='#2ca02c')
    plt.plot(iters_bis, x2_bis, label='x2 (точний корінь = 0.12)', linestyle='--', linewidth=2.0, color='#333333')
    
    plt.title('Зміна меж і поточного наближення кореня (метод половинного ділення, i = 0..10)', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('Номер ітерації (i)', fontsize=10, fontweight='bold')
    plt.ylabel('Значення', fontsize=10, fontweight='bold')
    plt.xticks(iters_bis)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='upper right')
    plt.tight_layout()
    
    bis_plot_path = os.path.join("Lab5", "plots", "bisection_plot.png")
    plt.savefig(bis_plot_path, dpi=300)
    plt.close()
    print(f"Bisection plot saved to: {bis_plot_path}")
    
    # 2. Newton Data (i = 0 to 5)
    newton_data = [
        (0, 0.0),
        (1, 0.13846153846153844),
        (2, 0.12032247228753779),
        (3, 0.12000010188496674),
        (4, 0.12000000000001018),
        (5, 0.12)
    ]
    
    iters_newt = [d[0] for d in newton_data]
    x_vals = [d[1] for d in newton_data]
    x2_newt = [0.12 for _ in iters_newt]
    
    plt.figure(figsize=(9.5, 5.5), dpi=300)
    plt.plot(iters_newt, x_vals, label='x (поточне наближення)', marker='o', markersize=7, linewidth=2.0, color='#1f77b4')
    plt.plot(iters_newt, x2_newt, label='x2 (точний корінь = 0.12)', linestyle='--', linewidth=2.0, color='#d62728')
    
    plt.title('Зміна поточного наближення кореня (метод Ньютона)', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('Номер ітерації (i)', fontsize=10, fontweight='bold')
    plt.ylabel('Значення кореня x', fontsize=10, fontweight='bold')
    plt.xticks(iters_newt)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='upper right')
    plt.tight_layout()
    
    newt_plot_path = os.path.join("Lab5", "plots", "newton_plot.png")
    plt.savefig(newt_plot_path, dpi=300)
    plt.close()
    print(f"Newton plot saved to: {newt_plot_path}")

if __name__ == "__main__":
    generate_plots()
