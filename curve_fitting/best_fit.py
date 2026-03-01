import numpy as np
import matplotlib.pyplot as plt

def fit_linear(x, y):
    n = len(x)
    x_ = np.sum(x) / n
    y_ = np.sum(y) / n
    a = np.sum((x - x_) * (y - y_)) / np.sum((x - x_)**2)
    b = y_ - a * x_
    y_pred = a * x + b 
    sse = np.sum((y - y_pred)**2)    
    return a, b, sse, lambda xi: a * xi + b, f"y = {a:.4f}x + {b:.4f}"

def fit_quadratic(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum(x**2 * y)
    A = np.array([
        [sum_x4, sum_x3, sum_x2],
        [sum_x3, sum_x2, sum_x],
        [sum_x2, sum_x, n]
    ])
    B = np.array([sum_x2y, sum_xy, sum_y])
    coeffs = np.linalg.solve(A, B)
    a, b, c = coeffs
    y_pred = a * x**2 + b * x + c 
    sse = np.sum((y - y_pred)**2)
    return a, b, sse, lambda xi: a * xi**2 + b * xi + c, f"y = {a:.4f}x² + {b:.4f}x + {c:.4f}"

def fit_exponential(x, y):
    try:
        ln_y = np.log(y)
        n = len(x)
        x_mean = np.sum(x) / n 
        ln_y_mean = np.sum(ln_y) / n 
        b = np.sum((x - x_mean) * (ln_y - ln_y_mean)) / np.sum((x - x_mean)**2)
        ln_a = ln_y_mean - b * x_mean
        a = np.exp(ln_a)
        y_pred = a * np.exp(b * x)
        sse = np.sum((y - y_pred)**2)
        return a, b, sse, lambda xi: a * np.exp(b * xi), f"y = {a:.4f}e^({b:.4f}x)"
    except:
        return None, None, float('inf'), None, "Exponential fit failed"

def fit_logarithmic(x, y):
    try:
        ln_x = np.log(x)
        n = len(x)
        ln_x_mean = np.sum(ln_x) / n
        y_mean = np.sum(y) / n
        b = np.sum((ln_x - ln_x_mean) * (y - y_mean)) / np.sum((ln_x - ln_x_mean)**2)
        a = y_mean - b * ln_x_mean
        y_pred = a + b * np.log(x)
        sse = np.sum((y - y_pred)**2)
        return a, b, sse, lambda xi: a + b * np.log(xi), f"y = {a:.4f} + {b:.4f}ln(x)"
    except:
        return None, None, float('inf'), None, "Logarithmic fit failed"

def fit_power(x, y):
    try:
        ln_x = np.log(x)
        ln_y = np.log(y)
        n = len(x)
        ln_x_mean = np.sum(ln_x) / n
        ln_y_mean = np.sum(ln_y) / n
        b = np.sum((ln_x - ln_x_mean) * (ln_y - ln_y_mean)) / np.sum((ln_x - ln_x_mean)**2)
        ln_a = ln_y_mean - b * ln_x_mean
        a = np.exp(ln_a)
        y_pred = a * x**b
        sse = np.sum((y - y_pred)**2)
        return a, b, sse, lambda xi: a * xi**b, f"y = {a:.4f}x^{b:.4f}"
    except:
        return None, None, float('inf'), None, "Power fit failed"

def main():
    x = np.array([1, 2, 3, 4, 5, 6, 7])
    y = np.array([87, 97, 113, 129, 202, 195, 193])
    models = {
        "Linear": fit_linear(x, y),
        "Quadratic": fit_quadratic(x, y),
        "Exponential": fit_exponential(x, y),
        "Logarithmic": fit_logarithmic(x, y),
        "Power": fit_power(x, y)
    }
  
    best_model = min(models.items(), key=lambda item: item[1][2])
    best_name = best_model[0]
    best_a, best_b, best_sse, best_func, best_eq = best_model[1]
    print(models)
    print(f"BEST FIT: {best_name}")
    print(f"Equation: {best_eq}")
    print(f"SSE: {best_sse:.6f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', s=100, marker='*', 
                label='Observed Data', zorder=5)
    x_smooth = np.linspace(x.min(), x.max(), 200)
    y_smooth = best_func(x_smooth)
    plt.plot(x_smooth, y_smooth, 'b-', linewidth=2, 
             label=f'Best Fit: {best_name}')
    y_pred = best_func(x)
    for i in range(len(x)):
        plt.plot([x[i], x[i]], [y[i], y_pred[i]], 
                'k--', alpha=0.5, linewidth=1)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Curve Fitting: {best_eq}\nSSE = {best_sse:.6f}', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
