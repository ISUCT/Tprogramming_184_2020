import matplotlib.pyplot as plt
import math

def calc(a, b, x):
    numerator = math.asin(math.pow(x,a))-math.acos(math.pow(x,b))
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
    a = 2
    b = 3
    xn = -1
    xk = 0.36
    dx = 0.05

    y = calc(a, b, xn)
    print(f'x={xn:.3f} y={y:.3f}')

    a_res = task_a(a, b, xn, xk, dx)
    print(a_res)

    x_arr = [0.08, 0.26, 0.35, 0.41, 0.53]
    b_res = task_b(a, b, x_arr)
    print(b_res)

    plt.plot(*zip(*a_res), 'b')
    plt.plot(*zip(*b_res), 'r')
    plt.show()