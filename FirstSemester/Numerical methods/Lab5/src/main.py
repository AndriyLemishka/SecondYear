import math

def fun(x):
    return x**2 + 0.78 * x - 0.108

def dfun(x):
    return 2 * x + 0.78

def bisection(a, b, delta):
    fa = fun(a)
    signa = int(math.copysign(1, fa))
    fb = fun(b)
    signb = int(math.copysign(1, fb))
    eps0 = 0
    
    for i in range(60):
        c = (a + b) / 2
        fc = fun(c)
        signc = int(math.copysign(1, fc))
        eps = abs(a - b)
        
        print(i, a, signa, b, signb, c, signc)
        
        if eps < delta:
            break
        if signb * signc > 0:
            b = c
            signb = signc
        else:
            a = c
            signa = signc
        eps0 = eps

def newton(x, delta):
    eps0 = 0
    
    print(0, x) 
    for i in range(1, 20):
        f = fun(x)
        df = dfun(x)
        x1 = x - f / df
        eps = abs(x1 - x)
        ksi = 2 * eps / (abs(x1) + delta)
        
        print(i, f, df, x1)
        
        if eps < delta or ksi < delta:
            break
        eps0 = eps
        x = x1

if __name__ == "__main__":
    bisection(0, 0.35, 1e-10)
    print()
    newton(0, 1e-10)
    print()
