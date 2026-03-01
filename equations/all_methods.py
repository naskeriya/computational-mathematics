import math

def f(x):
    return math.log(x)+x -2

def method_seq(method, a=None, b=None, x0=None, x1=None, tol=1e-4, max_iter=100):
    if method == "bisection":
        seq = [(a, f(a))]
        fa, fb = f(a), f(b)
        if fa * fb > 0:
            raise ValueError("interval does not have a root")
        for _ in range(max_iter):
            c = 0.5 * (a + b)
            fc = f(c)
            seq.append((c, fc))
            if abs(fc) < tol:
                break
            if fa * fc <= 0:
                b, fb = c, fc
            else:
                a, fa = c, fc
        return seq

    if method == "false_position":
        seq = [(a, f(a))]
        fa, fb = f(a), f(b)
        if fa * fb > 0:
            raise ValueError("interval does not have a root")
        for _ in range(max_iter):
            if fb - fa == 0: 
                break
            c = (a * fb - b * fa) / (fb - fa) # false position formula
            fc = f(c)
            seq.append((c, fc))
            if abs(fc) < tol:
                break
            if fa * fc < 0:
                b, fb = c, fc
            else:
                a, fa = c, fc
        return seq

    if method == "newton":
        seq = [(x0, f(x0))]
        x = x0
        for _ in range(max_iter):
            fp = f(x)
            df = -2*x*math.exp(-x**2) # derivative of f  
            if df == 0:
                break
            x_new = x - fp / df # Newton's formula
            if abs(x_new - x) < tol:
                break
            seq.append((x_new, f(x_new)))
            x = x_new
        return seq

    if method == "secant":
        seq = [(x0, f(x0)), (x1, f(x1))]
        iterations = 0 
        while iterations < (max_iter - 1):
            if f(x1) - f(x0) == 0: 
                break
            x_temp = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) # Secant formula
            x0, x1 = x1, x_temp
            if abs(x1 - x0) < tol:
                break
            seq.append((x1, f(x1)))
            iterations += 1
        return seq

def pad_seq(seq, length=7):
    out = list(seq)
    while len(out) < length:
        out.append((None, None))
    return out[:length]

def print_comparison_table():
    a_bis, b_bis = -5, 5  
    x0_newton = 0.5          
    x0_sec0, x0_sec1 = 1, 2  
    ITERS = 25 
    rows = ITERS + 1 

    bis = pad_seq(method_seq("bisection", a=a_bis, b=b_bis, max_iter=ITERS), rows) # rows
    new = pad_seq(method_seq("newton", x0=x0_newton, max_iter=ITERS), rows)
    sec = pad_seq(method_seq("secant", x0=x0_sec0, x1=x0_sec1, max_iter=ITERS), rows)
    fals = pad_seq(method_seq("false_position", a=a_bis, b=b_bis, max_iter=ITERS), rows)

    header = ("Iter", "Bisection", "f(Bis)", "Newton", "f(Newt)", "Secant", "f(Sec)", "FalsePos", "f(False)")
    print("{:>4s} | {:>10s} {:>12s} | {:>12s} {:>12s} | {:>10s} {:>12s} | {:>12s} {:>12s}".format(*header))
    print("-" * 113)
    for i in range(rows):
        bx, bf = bis[i]
        nx, nf = new[i]
        sx, sf = sec[i]
        fx, ff = fals[i]

        bx_str = f"{bx:10.6f}" if bx is not None else " " * 10
        bf_str = f"{bf:12.6f}" if bf is not None else " " * 12
        nx_str = f"{nx:12.6f}" if nx is not None else " " * 12
        nf_str = f"{nf:12.6f}" if nf is not None else " " * 12
        sx_str = f"{sx:10.6f}" if sx is not None else " " * 10
        sf_str = f"{sf:12.6f}" if sf is not None else " " * 12
        fx_str = f"{fx:12.6f}" if fx is not None else " " * 12
        ff_str = f"{ff:12.6f}" if ff is not None else " " * 12

        print(f"{i:4d} | {bx_str} {bf_str} | {nx_str} {nf_str} | {sx_str} {sf_str} | {fx_str} {ff_str}")

if __name__ == "__main__":
    print_comparison_table()