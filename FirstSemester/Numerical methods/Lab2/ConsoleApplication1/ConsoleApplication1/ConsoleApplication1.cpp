#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Поліном Лагранжа 1-го порядку (за вузлами X4, X5)
double lagrange1(double x) {
    return -0.35555556 * x + 0.44;
}

// Поліном Лагранжа 2-го порядку (за вузлами X3, X4, X5)
double lagrange2(double x) {
    return 0.2962963 * x * x - 0.8222222 * x + 0.62;
}

// Поліном Лагранжа 3-го порядку (за вузлами X2, X3, X4, X5)
double lagrange3(double x) {
    return 6.438043 * x * x * x - 12.740741 * x * x + 7.651852 * x - 1.14;
}

// Поліном Лагранжа 4-го порядку (за вузлами X1, X2, X3, X4, X5)
double lagrange4(double x) {
    return 23.248489 * pow(x, 4) - 45.871056 * pow(x, 3)
        + 28.452675 * x * x - 5.588889 * x + 0.29;
}

int main() {
    const double xmin = 0.0;
    const double xmax = 0.9;
    const int points = 50;
    const double h = (xmax - xmin) / points;

    cout << setprecision(17);
    for (int i = 0; i <= points; ++i) {
        double x = xmin + i * h;
        double y1 = lagrange1(x);
        double y2 = lagrange2(x);
        double y3 = lagrange3(x);
        double y4 = lagrange4(x);
        cout << x << " " << y1 << " " << y2 << " " << y3 << " " << y4 << "\n";
    }
    return 0;
}
