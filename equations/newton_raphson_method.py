import math

def f(x):
    return x ** 3 - 2 * x - 5

def f_prime(x):
    return 3 * x ** 2 - 2

def newton_raphson(x0, tolerance=0.0001, max_iterations=100):
    iterations = []
    for i in range(max_iterations):
        x1 = x0 - f(x0) / f_prime(x0) 
        iterations.append((i + 1, x1))
        if abs(x1 - x0) < tolerance: 
            break
        x0 = x1
    return x1, iterations

x0 = 2
root, intermediate_steps = newton_raphson(x0)
print(f"Root: {root:.4f}")
print("Iterations:")
for step in intermediate_steps:
    print(f"Iteration {step[0]}: x = {step[1]:.6f}")