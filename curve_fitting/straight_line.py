import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2.4, 3.5, 5.1, 6.0], dtype=float)

n = len(x)
x_mean = np.sum(x) / n
y_mean = np.sum(y) / n

a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
b = y_mean - a * x_mean

y_pred = a * x + b
sse = np.sum((y - y_pred)**2)

print(f"a = {a:.4f}, b = {b:.4f}")
print(f"Equation: y = {a:.4f}x + {b:.4f}")
print(f"SSE = {sse:.6f}")

x_smooth = np.linspace(x.min(), x.max(), 200)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', s=100, marker='*', label='Data', zorder=5)
plt.plot(x_smooth, a * x_smooth + b, 'b-', linewidth=2, label=f'y = {a:.4f}x + {b:.4f}')
for i in range(n):
    plt.plot([x[i], x[i]], [y[i], y_pred[i]], 'k--', alpha=0.5)
plt.title(f'Task 1: Linear Fit\ny = {a:.4f}x + {b:.4f} | SSE = {sse:.6f}')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True, alpha=0.3); plt.tight_layout(); plt.show()