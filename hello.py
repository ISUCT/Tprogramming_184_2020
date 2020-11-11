import matplotlib.pyplot as plt
import math

def calc(a, b, x):
    numerator = (a * x**(1/3) - b * math.log(x, 5)) / (math.log10(x-1))**3
    return numerator

def task_a(a, b, xn, xk, dx):
    x = xn
    result = []
    while x <= xk:
        y = calc(a, b, x)
        result.append([x, y])
        x += dx
    return result

def task_b(a, b, x_arr):
    result = []
    for x in x_arr:
        y = calc(a, b, x)
        result.append([x, y])
    return result


if __name__ == "__main__":
    a = 4.1
    b = 2.7
    xn = 1.5
    xk = 3.5
    dx = 0.4

    y = calc(a, b, xn)
    print(f'x={xn:.3f} y={y:.3f}')

    a_res = task_a(a, b, xn, xk, dx)
    print(a_res)

    x_arr = [1.9, 2.15, 2.34, 2.74, 3.16]
    b_res = task_b(a, b, x_arr)
    print(b_res)

    plt.plot(*zip(*a_res), 'b')
    plt.plot(*zip(*b_res), 'r')
    plt.show()