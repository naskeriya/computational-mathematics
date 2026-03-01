import numpy as np
import matplotlib.pyplot as plt

def g1(x):
    return np.log(x + 3) 

def g1_prime(x):
    return 1 / (x + 3)

def g2(x):
    val = -np.log(x + 1)
    return np.sqrt(val) if val >= 0 else np.nan

def g2_prime(x):
    return -1 / (2 * (x + 1) * np.sqrt(-np.log(x + 1)))

def g3(x):
    if x == 0:
        return np.nan
    return -np.log(x + 1) / x

def g3_prime(x):
    if x == 0:
        return np.nan
    return (np.log(x + 1) - 1) / (x**2)

def check_convergence_condition(g_prime, a, b, num_points=100):
    x_vals = np.linspace(a, b, num_points)
    g_prime_vals = [abs(g_prime(x)) for x in x_vals]
    max_derivative = max(g_prime_vals)
    satisfies = max_derivative < 1
    return satisfies, max_derivative, g_prime_vals

def fixed_point_iteration(g, x0, tol=0.001, max_iter=100):
    iterations = [x0]
    errors = []
    
    for i in range(max_iter):
        try:
            x_new = g(iterations[-1])
            if np.isnan(x_new):
                break
            error = abs(x_new - iterations[-1])
            errors.append(error)
            iterations.append(x_new)
            if error < tol:
                return iterations, errors, True
        except:
            break
    return iterations, errors, False


x0 = 1
tol = 0.001
a, b = 0, 1

forms = [
    ("g1(x) = -ln(x + 1)", g1, g1_prime),
    ("g2(x) = sqrt(-ln(x + 1))", g2, g2_prime),
    ("g3(x) = -ln(x + 1) / x", g3, g3_prime)
]

results = {}

for name, g, g_prime in forms:
    print(f"\n{name}")
    print("-" * 70)
    
    satisfies, max_deriv, deriv_vals = check_convergence_condition(g_prime, a, b)
    print(f"Convergence Condition |g'(x)| < 1 on [0,1]: {satisfies}")
    print(f"Max |g'(x)| = {max_deriv:.6f}")
    
    iterations, errors, converged = fixed_point_iteration(g, x0, tol)
    
    print(f"\nIterations from x0 = {x0}:")
    for i, (x, err) in enumerate(zip(iterations[:10], errors[:10])):
        print(f"  x{i} = {x:.6f}, error = {err:.6f}")
    
    if converged:
        print(f"\nConverged after {len(iterations)-1} iterations")
        print(f"Final root ≈ {iterations[-1]:.6f}")
    else:
        print(f"\nDid NOT converge within {len(iterations)-1} iterations")
    
    results[name] = {
        'converged': converged,
        'iterations': iterations,
        'errors': errors,
        'max_deriv': max_deriv
    }

print("\n" + "=" * 70)
print("PERFORMANCE COMPARISON")
print("=" * 70)
print(f"{'Form':<30} {'Converged':<12} {'Iterations':<12} {'Max g\'(x)':<12}")
print("-" * 70)
for name, data in results.items():
    n_iter = len(data['iterations']) - 1 if data['converged'] else "N/A"
    print(f"{name:<30} {str(data['converged']):<12} {str(n_iter):<12} {data['max_deriv']:<12.6f}")