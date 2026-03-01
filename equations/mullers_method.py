import numpy as np

def f(x):
    return x**4 - 3*x**3 + x**2 + x + 1

def mullers_method(x0, x1, x2, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        f0, f1, f2 = f(x0), f(x1), f(x2)
        h0, h1 = x1 - x0, x2 - x1
        d0 = (f1 - f0) / h0
        d1 = (f2 - f1) / h1
        d2 = (d1 - d0) / (h1 + h0)

        a = d2
        b = d1 + h1 * d2
        c = f2

        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            continue  

        sqrt_disc = np.sqrt(discriminant)
        x3_1 = x2 + (-2*c) / (b + sqrt_disc)
        x3_2 = x2 + (-2*c) / (b - sqrt_disc)

        x3 = x3_1 if abs(f(x3_1)) < abs(f(x3_2)) else x3_2

        if abs(x3 - x2) < tol:
            return x3

        x0, x1, x2 = x1, x2, x3

    return None  

if __name__ == "__main__":
    root = mullers_method(0, 1, 2)
    print(f"Found root: {root}")