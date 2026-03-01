import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4], dtype=float)
y = np.array([3.0, 4.8, 9.0, 15.5], dtype=float)

n = len(x)
sum_x  = np.sum(x)
sum_x2 = np.sum(x**2)
sum_x3 = np.sum(x**3)
sum_x4 = np.sum(x**4)
sum_y   = np.sum(y)
sum_xy  = np.sum(x * y)
sum_x2y = np.sum(x**2 * y)

A = np.array([
    [sum_x4, sum_x3, sum_x2],
    [sum_x3, sum_x2, sum_x],
    [sum_x2, sum_x,  n]
])
B = np.array([sum_x2y, sum_xy, sum_y])

a, b, c = np.linalg.solve(A, B)

y_pred = a * x**2 + b * x + c
sse = np.sum((y - y_pred)**2)

print(f"a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")
print(f"Equation: y = {a:.4f}x² + {b:.4f}x + {c:.4f}")
print(f"SSE = {sse:.6f}")

x_smooth = np.linspace(x.min(), x.max(), 200)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', s=100, marker='*', label='Data', zorder=5)
plt.plot(x_smooth, a * x_smooth**2 + b * x_smooth + c, 'b-', linewidth=2,
         label=f'y = {a:.4f}x² + {b:.4f}x + {c:.4f}')
for i in range(n):
    plt.plot([x[i], x[i]], [y[i], y_pred[i]], 'k--', alpha=0.5)
plt.title(f'Task 2: Quadratic Fit\ny = {a:.4f}x² + {b:.4f}x + {c:.4f} | SSE = {sse:.6f}')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True, alpha=0.3); plt.tight_layout(); plt.show()