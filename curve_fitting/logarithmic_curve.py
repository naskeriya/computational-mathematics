import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2.1, 3.0, 3.6, 4.2], dtype=float)

n = len(x)
ln_x = np.log(x)
ln_x_mean = np.sum(ln_x) / n
y_mean    = np.sum(y) / n

b = np.sum((ln_x - ln_x_mean) * (y - y_mean)) / np.sum((ln_x - ln_x_mean)**2)
a = y_mean - b * ln_x_mean

y_pred = a + b * np.log(x)
sse = np.sum((y - y_pred)**2)

print(f"a = {a:.4f}, b = {b:.4f}")
print(f"Equation: y = {a:.4f} + {b:.4f}ln(x)")
print(f"SSE = {sse:.6f}")

x_smooth = np.linspace(x.min(), x.max(), 200)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', s=100, marker='*', label='Data', zorder=5)
plt.plot(x_smooth, a + b * np.log(x_smooth), 'b-', linewidth=2,
         label=f'y = {a:.4f} + {b:.4f}ln(x)')
for i in range(n):
    plt.plot([x[i], x[i]], [y[i], y_pred[i]], 'k--', alpha=0.5)
plt.title(f'Task 4: Logarithmic Fit\ny = {a:.4f} + {b:.4f}ln(x) | SSE = {sse:.6f}')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True, alpha=0.3); plt.tight_layout(); plt.show()