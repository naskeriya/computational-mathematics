import math

def function(x):
    return x**3 -3*x + 1

def bisection(a, b, tol=0.001, max_iter=100):
    fa, fb = function(a), function(b)
    if fa * fb > 0:
        print("no sign change")
        return None, []
    if abs(fa) < tol: 
        print("the root is at left endpoint", a)
        return a, []
    if abs(fb) < tol:
        print("the root is at right endpoint", b)
        return b, []
    history = []
    for i in range(1, max_iter + 1): 
        c = (a + b) / 2 
        fc = function(c) 
        history.append((i, a, b, c, fc)) 
        if abs(fc) < tol or (b - a) < tol: 
            return c, history
        if fa * fc < 0: 
            b, fb = c, fc
        else: 
            a, fa = c, fc
    return c, history

root, history = bisection(0, 1, tol=0.001, max_iter=100)
print(f"Root: {root:.4f}")
print("Iterations:")
for step in history:
    i, a, b, c, fc = step
    print(f"Iteration {i}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6e}")
