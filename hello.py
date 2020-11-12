import matplotlib.pyplot as plt
import math

def calc(a, b, x):
    numerator = math.acos(x**2 - b**2)
    denomerator = math.asin(x**2 - a**2)
    y = numerator/denomerator

    return y

def task_a(a, b, xn, xk, dx):
    x = xn
    res = []

    while x <= xk:
        y = calc(a, b, x)
        res.append((x, y))
        x += dx

    return res

def task_b(a, b, x_arr):
    res = []

    for x in x_arr:
        y = calc(a, b, x)
        res.append((x, y))

    return res

if __name__ == "__main__" :
    a = 0.05
    b = 0.06
    x = 0.2

    a_res = task_a(a, b, 0.2, 0.95, 0.15)
    form_a_res = ['%.2f' % x[0] for x in a_res]
    print(*form_a_res, sep=' ')

    x_arr = [0.15, 0.26, 0.37, 0.48, 0.56]
    b_res = task_b(a, b, x_arr)
    form_b_res = ['%.2f' % x[0] for x in b_res]
    print(*form_b_res, sep=' ')

    plt.plot(*zip(*a_res), 'b')
    plt.plot(*zip(*b_res), 'r')
    plt.show()