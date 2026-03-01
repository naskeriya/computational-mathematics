import numpy as np

def lagrange_interpolation(x_data, y_data, x_target):
    n = len(x_data)
    result = 0.0
    print("LAGRANGE INTERPOLATION")
    print(f"\n{'i':^5} {'x_i':^12} {'y_i':^12} {'L_i(x*)':^15} {'y_i × L_i(x*)':^15}")
    print("-"*80)

    for i in range(n): 
        L_i = 1.0 
        for j in range(n): 
            if i != j: 
                L_i *= (x_target - x_data[j]) / (x_data[i] - x_data[j]) 
        contribution = y_data[i] * L_i 
        result += contribution 
        print(f"{i:^5} {x_data[i]:^12.4f} {y_data[i]:^12.6f} {L_i:^15.8f} {contribution:^15.8f}")
    print("-"*80)
    print(f"\nInterpolated value: y({x_target}) = {result:.4f}\n")
    return result

def newton_forward(x_data, y_data, x_target):
    n = len(x_data)
    h = x_data[1] - x_data[0]
    u = (x_target - x_data[0]) / h 
    print("NEWTON'S FORWARD DIFFERENCE INTERPOLATION")
    diff = np.zeros((n, n))
    diff[:, 0] = y_data 

    for j in range(1, n): 
        for i in range(n - j): 
            diff[i, j] = diff[i + 1, j - 1] - diff[i, j - 1] 
    print(f"{'x':^10}", end="") 
    print(f"{'y':^12}", end="")

    for j in range(1, n):
        print(f"{'Δ^' + str(j) + 'y':^12}", end="") 
    print("\n" + "-"*80)

    for i in range(n):
        print(f"{x_data[i]:^10.4f}", end="")
        for j in range(n):
            if i + j < n:
                print(f"{diff[i, j]:^12.6f}", end="")
            else:
                print(f"{'':^12}", end="")
        print()
    print("-"*80)
    result = diff[0, 0] 
    u_term = 1.0

    for k in range(1, n):
        u_term *= (u - k + 1) / k 
        result += u_term * diff[0, k] 
    print(f"\nInterpolated value: y({x_target}) = {result:.4f}\n")
    return result

def newton_backward(x_data, y_data, x_target):
    n = len(x_data)
    h = x_data[1] - x_data[0]
    v = (x_target - x_data[-1]) / h
    print("NEWTON'S BACKWARD DIFFERENCE INTERPOLATION")
    diff = np.zeros((n, n))
    diff[:, 0] = y_data

    for j in range(1, n):
        for i in range(j, n):
            diff[i, j] = diff[i, j - 1] - diff[i - 1, j - 1]
    print(f"{'x':^10}", end="")
    print(f"{'y':^12}", end="")

    for j in range(1, n):
        print(f"{'∇^' + str(j) + 'y':^12}", end="")
    print("\n" + "-"*80)

    for i in range(n):
        print(f"{x_data[i]:^10.4f}", end="")
        for j in range(n):
            if i >= j:
                print(f"{diff[i, j]:^12.6f}", end="")
            else:
                print(f"{'':^12}", end="")
        print()
    print("-"*80)
    result = diff[-1, 0]
    v_term = 1.0

    for k in range(1, n):
        v_term *= (v + k - 1) / k
        result += v_term * diff[-1, k]
    print(f"\nInterpolated value: y({x_target}) = {result:.4f}\n")
    return result

def interpolate(x_data, y_data, x_target):
    x_data = np.array(x_data, dtype=float) 
    y_data = np.array(y_data, dtype=float)

    if not np.all(x_data[:-1] <= x_data[1:]): 
        sorted_indices = np.argsort(x_data) 
        x_data = x_data[sorted_indices]
        y_data = y_data[sorted_indices] 
    differences = np.diff(x_data)
    is_uniform = np.allclose(differences, differences[0], rtol=1e-6, atol=1e-6) 

    if is_uniform:
        newton_forward(x_data, y_data, x_target)
        newton_backward(x_data, y_data, x_target)
    else:
        lagrange_interpolation(x_data, y_data, x_target)

def main():
    x_data = [100, 150, 200, 250, 300, 350, 400]
    y_data = [10.63, 13.03, 15.04, 16.81, 18.42, 19.90, 21.27] 
    x_target = 410
    interpolate(x_data, y_data, x_target)

if __name__ == "__main__":
    main()