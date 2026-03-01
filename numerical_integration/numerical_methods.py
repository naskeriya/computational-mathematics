import numpy as np

def trapezoidal_rule(f, x0, xn, n):
    h = (xn - x0) / n 
    sum_val = 0 
    for i in range(1, n):
        xi = x0 + i * h
        sum_val += f(xi)
    area = (h / 2) * (f(x0) + 2 * sum_val + f(xn))
    return area

def simpson_one_third_rule(f, x0, xn, n):
    if n % 2 != 0:
        n = n + 1
    h = (xn - x0) / n
    sum_odd = 0
    sum_even = 0
    for i in range(1, n):
        xi = x0 + i * h
        if i % 2 == 1:
            sum_odd += f(xi)
        else:
            sum_even += f(xi)
    area = (h / 3) * (f(x0) + 4 * sum_odd + 2 * sum_even + f(xn))
    return area

def simpson_three_eighth_rule(f, x0, xn, n):
    if n % 3 != 0:
        n = n + (3 - n % 3)
    h = (xn - x0) / n
    sum_non_mult_3 = 0
    sum_mult_3 = 0
    for i in range(1, n):
        xi = x0 + i * h
        if i % 3 == 0:
            sum_mult_3 += f(xi)
        else:
            sum_non_mult_3 += f(xi)
    area = (3 * h / 8) * (f(x0) + 3 * sum_non_mult_3 + 2 * sum_mult_3 + f(xn))
    return area

def newton_cotes_rule(f, x0, xn, n):
    h = (xn - x0) / n 
    nodes = [x0 + i * h for i in range(n + 1)]
    def lagrange_weight(i, nodes, x0, xn):
        n_points = len(nodes)
        num_samples = 1000
        h_sample = (xn - x0) / num_samples
        weight = 0
        for k in range(num_samples + 1):
            x = x0 + k * h_sample
            L_i = 1.0
            for j in range(n_points):
                if j != i:
                    L_i *= (x - nodes[j]) / (nodes[i] - nodes[j])
            if k == 0 or k == num_samples:
                weight += 0.5 * h_sample * L_i
            else:
                weight += h_sample * L_i
        return weight
    integral = 0
    for i in range(n + 1):
        weight = lagrange_weight(i, nodes, x0, xn)
        integral += weight * f(nodes[i])
    return integral


def numerical_integration(f, a, b, n):
    results = {}
    n_trap = n
    n_simp13 = n if n % 2 == 0 else n + 1
    n_simp38 = n if n % 3 == 0 else n + (3 - n % 3)
    n_nc = n
    results['newton'] = newton_cotes_rule(f, a, b, n_nc)
    results['simp13'] = simpson_one_third_rule(f, a, b, n_simp13)
    results['simp38'] = simpson_three_eighth_rule(f, a, b, n_simp38)
    results['trap'] = trapezoidal_rule(f, a, b, n_trap)
    return results


def main():
    f1 = np.sin
    a1, b1 = 0, np.pi/2
    n1 = 10
    results1 = numerical_integration(f1, a1, b1, n1)
    print(f"1) Newton-Cotes = {results1['newton']:.10f}")
    print(f"2) Simpson 1/3 = {results1['simp13']:.10f}")
    print(f"3) Simpson 3/8 = {results1['simp38']:.10f}")
    print(f"4) Trapezoidal = {results1['trap']:.10f}")

if __name__ == "__main__":
    main()