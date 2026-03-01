import matplotlib.pyplot as plt
import numpy as np

def functions(x):
    func1 = np.tan(x) 
    func2 = x ** 2
    return func1, func2

def intersection_points(interval, func1, func2):
    points = []
    for i in range(1, len(interval)): 
        if (func1[i-1] - func2[i-1]) * (func1[i] - func2[i]) < 0: 
            points.append((interval[i-1] + interval[i]) / 2) 
    return points

def plot_functions(interval, func1, func2, points):
    plt.plot(interval, func1, label='tan(x)', color='blue')
    plt.plot(interval, func2, label='x^2', color='orange')
    for xi in points:
        plt.plot(xi, np.tan(xi), 'ro')  
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of tan(x) and x^2')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    x_min, x_max = 0.5 , 1.5 
    interval = np.linspace(x_min, x_max) 
    func1, func2 = functions(interval) 
    points = intersection_points(interval, func1, func2) 
    plot_functions(interval, func1, func2, points) 
    print("Intersection points:", points) 

if __name__ == "__main__":
    main() 
    