def gauss(AA, BB):
    n = len(BB)
    A = []
    for aa in AA:
        A.append(aa[:])
    B = BB[:]
    
    # прямий хід алгоритму
    for k in range(n - 1):
        
        # визначення найбільшого елемента
        value = 0
        index = 0
        for i in range(k, n):
            if abs(A[i][k]) > value:
                value = abs(A[i][k])
                index = i
        
        # перестановка рядків
        A[k], A[index] = A[index], A[k]
        B[k], B[index] = B[index], B[k]
    
        # перевірка умови
        if A[k][k] == 0:
            print("Error: A[k][k] == 0")
            return
    
        # побудова трикутної матриці
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - A[k][j] * m
            B[i] = B[i] - B[k] * m

    # зворотній хід алгоритму 
    X = B[:]
    X[n - 1] = B[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            X[i] = X[i] - A[i][j] * X[j]
        X[i] = X[i] / A[i][i]
    print(X)

    
def gauss_seidel(A, B, X0, delta):
    dimension = len(X0)
    X = X0[:]
    print(0, X)
    
    for k in range(1, 40):
        for i in range(dimension):
            X[i] = B[i]
            for j in range(dimension):
                if i != j:
                    X[i] = X[i] - A[i][j] * X[j]
            X[i] = X[i] / A[i][i]

        eps = []
        ksi = []
        for i in range(dimension):
            eps.append(abs(X[i] - X0[i]))
            ksi.append(eps[i] / (abs(X[i]) + delta))
        X0 = X[:]
        eps_max = 0
        ksi_max = 0
        for i in range(dimension):
            if eps_max < eps[i]: eps_max = eps[i]
            if ksi_max < ksi[i]: ksi_max = ksi[i]
            
        print(k, X)

        if eps_max < delta and ksi_max < delta:
            break

A = [[1, 1, 1, 1, 1],
     [0, 2.1, 0, -0.9, -0.7],
     [-0.5, -0.9, 1.7, -0.4, -0.5],
     [0, -0.5, -0.5, 2.4, -0.3],
     [-0.2, -0.7, -0.6, -0.6, 1.8]]

B = [6, 0.6, -0.72, 1.32, -0.36]
X0 = [0 for i in range(5)]
delta = 1e-10

gauss(A, B)

gauss_seidel(A, B, X0, delta)
