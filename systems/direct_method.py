def solve_system(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)] 
    EPS = 1e-4

    for i in range(n): 
        pivot_row = i

        for j in range(i + 1, n): 
            if abs(M[j][i]) > abs(M[pivot_row][i]):
                pivot_row = j
        M[i], M[pivot_row] = M[pivot_row], M[i]

        if abs(M[i][i]) < EPS: 
            break

        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n + 1):
                M[j][k] -= factor * M[i][k]

    rank = 0 

    for i in range(n):
        if all(abs(M[i][j]) < EPS for j in range(n)):
            if abs(M[i][n]) > EPS:
                print("No solution (inconsistent system)")
                return
        else:
            rank += 1

    x_particular = [0] * n
    free_vars = []
    pivot_cols = []

    for i in range(n - 1, -1, -1):
        pivot_col = -1
        for j in range(n):
            if abs(M[i][j]) > EPS:
                pivot_col = j
                break
        if pivot_col == -1:
            continue
        pivot_cols.append(pivot_col)
        sum_known = sum(M[i][j] * x_particular[j] for j in range(pivot_col + 1, n))
        x_particular[pivot_col] = (M[i][n] - sum_known) / M[i][pivot_col]

    free_vars = [j for j in range(n) if j not in pivot_cols] 
    params = ['s', 't', 'u', 'v'][:len(free_vars)]
    basis_vectors = []

    for free_col in free_vars:
        vec = [0] * n
        vec[free_col] = 1
        for row in range(n):
            pivot_col = -1
            for col in range(n):
                if abs(M[row][col]) > EPS:
                    pivot_col = col
                    break

            if pivot_col != -1 and pivot_col != free_col:
                sum_known = sum(M[row][j] * vec[j] for j in range(n) if j != pivot_col)
                vec[pivot_col] = - (M[row][n] - sum_known) / M[row][pivot_col] if abs(M[row][pivot_col]) > EPS else 0
        basis_vectors.append(vec)

    def nice(x): 
        if abs(x) < EPS:
            return "0"
        if abs(x - round(x)) < EPS:
            return str(int(round(x)))
        return f"{x:.6f}".rstrip('0').rstrip('.')

    vars = ['x', 'y', 'z', 'w'][:n]
    print(f"[{', '.join(vars)}] = [{', '.join(nice(v) for v in x_particular)}]", end="")

    for i, vec in enumerate(basis_vectors):
        print(f" + {params[i]}[{', '.join(nice(v) for v in vec)}]", end="")
    print("\n")

    if len(pivot_cols) == n:
        det = 1
        for i in range(n):
            det *= M[i][i]
        print(f"Determinant = {nice(det)}\n")
    else:
        print("Determinant = 0\n")

    if len(pivot_cols) == n:
        inv_M = [A[i][:] + [1 if j == i else 0 for j in range(n)] for i in range(n)]
        for i in range(n):
            pivot = inv_M[i][i]
            for j in range(2 * n):
                inv_M[i][j] /= pivot
            for k in range(n):
                if k != i:
                    factor = inv_M[k][i]
                    for j in range(2 * n):
                        inv_M[k][j] -= factor * inv_M[i][j]
        inverse = [row[n:] for row in inv_M]
        print("Inverse matrix:")
        for row in inverse:
            print("[" + ", ".join(nice(x) for x in row) + "]")
        print()
        print("Proof: A × A⁻¹ = I")
        for i in range(n):
            row = []
            for j in range(n):
                val = sum(A[i][k] * inverse[k][j] for k in range(n))
                row.append(nice(val))
            print("[" + ", ".join(row) + "]")
    else:
        print("Inverse does not exist (matrix is singular)")

if __name__ == "__main__":
    A = [[1, 9, -5], [-3, -5, -5], [-2, -7, 1]]
    b = [-32, -10, 13]
    solve_system(A, b)