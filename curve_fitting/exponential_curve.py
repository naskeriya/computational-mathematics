import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2.0, 5.5, 14.8, 40.2], dtype=float)

n = len(x)
ln_y = np.log(y)
x_mean    = np.sum(x) / n
ln_y_mean = np.sum(ln_y) / n

b    = np.sum((x - x_mean) * (ln_y - ln_y_mean)) / np.sum((x - x_mean)**2)
ln_a = ln_y_mean - b * x_mean
a    = np.exp(ln_a)

y_pred = a * np.exp(b * x)
sse = np.sum((y - y_pred)**2)

print(f"a = {a:.4f}, b = {b:.4f}")
print(f"Equation: y = {a:.4f}e^({b:.4f}x)")
print(f"SSE = {sse:.6f}")

x_smooth = np.linspace(x.min(), x.max(), 200)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', s=100, marker='*', label='Data', zorder=5)
plt.plot(x_smooth, a * np.exp(b * x_smooth), 'b-', linewidth=2,
         label=f'y = {a:.4f}e^({b:.4f}x)')
for i in range(n):
    plt.plot([x[i], x[i]], [y[i], y_pred[i]], 'k--', alpha=0.5)
plt.title(f'Task 3: Exponential Fit\ny = {a:.4f}e^({b:.4f}x) | SSE = {sse:.6f}')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid(True, alpha=0.3); plt.tight_layout(); plt.show()