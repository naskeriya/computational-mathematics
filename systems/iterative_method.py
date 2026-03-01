def copy_matrix(matrix):
    return [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

def print_matrix(matrix):
    for row in matrix:
        print([round(val, 6) for val in row])

def calculate_determinant(A):
    n = len(A)
    matrix = copy_matrix(A)
    det = 1.0

    for k in range(n):
        max_row = k
        for i in range(k + 1, n):
            if abs(matrix[i][k]) > abs(matrix[max_row][k]):
                max_row = i
        if max_row != k:
            matrix[k], matrix[max_row] = matrix[max_row], matrix[k]
            det *= -1
        if abs(matrix[k][k]) < 1e-10:
            return 0
        det *= matrix[k][k]
        for i in range(k + 1, n): 
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, n):
                matrix[i][j] -= factor * matrix[k][j]
    return det

def calculate_inverse(A):
    n = len(A)
    aug = [A[i][:] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for k in range(n):
        max_row = k
        for i in range(k + 1, n):
            if abs(aug[i][k]) > abs(aug[max_row][k]):
                max_row = i
        if max_row != k:
            aug[k], aug[max_row] = aug[max_row], aug[k]
        if abs(aug[k][k]) < 1e-10:
            return None
        pivot = aug[k][k]
        for j in range(2 * n):
            aug[k][j] /= pivot
        for i in range(n):
            if i != k:
                factor = aug[i][k]
                for j in range(2 * n):
                    aug[i][j] -= factor * aug[k][j]
    inverse = [[aug[i][j + n] for j in range(n)] for i in range(n)]
    return inverse

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(A)
    if x0 is None:
        x = [0.0] * n
    else:
        x = x0[:]
    x_old = x[:]
    for k in range(max_iter):
        x_old = x[:]
        for i in range(n):
            if abs(A[i][i]) < 1e-10:
                return None, k, False
            sigma = 0
            for j in range(i):
                sigma += A[i][j] * x[j]
            for j in range(i + 1, n):
                sigma += A[i][j] * x_old[j]
            x[i] = (b[i] - sigma) / A[i][i]
        error = max(abs(x[i] - x_old[i]) for i in range(n))
        print(f"Iteration {k+1}: x = {[round(v, 8) for v in x]}, error = {error:.2e}")
        if error < tol:
            return x, k + 1, True
    return x, max_iter, False

def matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]
    return result

def verify_inverse(A, A_inv):
    product = matrix_multiply(A, A_inv)
    print("\nA * A^-1 =")
    print_matrix(product)

if __name__ == "__main__":
    A = [
        [10, 1, 1],
        [2, 10, 1],
        [2, 2, 10]
    ]
    b = [12, 13, 14]

    solution, iterations, converged = gauss_seidel(A, b, tol=1e-4, max_iter=50)

    if solution and converged:
        print("\n1) x =", [round(x, 6) for x in solution])
        det = calculate_determinant(A)
        print("\n2) det(A) =", round(det, 6))
        inverse = calculate_inverse(A)
        if inverse:
            print("\n3) A^-1 =")
            print_matrix(inverse)
            verify_inverse(A, inverse)