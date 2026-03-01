import math

def secant_method(f, x0, x1, tolerance=0.0001):
    iterations = 0
    values = [(x0, f(x0)), (x1, f(x1))]
    while abs(x1 - x0) >= tolerance:
        if f(x1) - f(x0) == 0: 
            break
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_temp
        values.append((x1, f(x1)))
        iterations += 1
    return x1, iterations, values

def func(x):
    return x - math.cos(x)

x0 = 0.7
x1 = 0.8
root, num_iterations, intermediate_values = secant_method(func, x0, x1)
print(f"Final approximation: {root:.4f}")
print(f"Number of iterations: {num_iterations}")
print("Intermediate values:")
for value in intermediate_values:
    print(f"x: {value[0]:.6f}, f(x): {value[1]:.6f}")