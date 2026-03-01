import math

def f(x):
    return x**5 + x**2 - 100

def false_position_method(x0, x1, iterations):
    for _ in range(iterations):
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1)) 
        print(f"Iteration {_ + 1}: x = {x2:.6f} fx = {f(x2):.6f}")
        if f(x2) * f(x0) < 0:
            x1 = x2
        else:
            x0 = x2    
    return x2

x0 = 2
x1 = 3
iterations = 100
root = false_position_method(x0, x1, iterations)
print(f"Approximate root: {root:.6f}")