import matplotlib.pyplot as plt
import math

def calc(a, b, x):
    if (x < 5):
        numerator = math.pow(math.log10(math.pow(a, 2) + x), 2)
        denominator = math.pow(a + x, 2)
        y = numerator / denominator
        return y
    else:
        numerator = math.pow(a + (b * x), 2.5)
        denominator = 1.8 + math.pow(math.cos(a * x), 3)
        y = numerator / denominator
        return y

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
    a = -2.5
    b = 3.4
    xn = 3.5
    xk = 6.5
    dx = 0.6

    y = calc(a, b, xn)
    print(f'x={xn:.3f} y={y:.3f}')

    a_res = task_a(a, b, xn, xk, dx)
    print(a_res)

    x_arr = [2.89, 3.54, 5.21, 6.28, 3.48]
    b_res = task_b(a, b, x_arr)
    print(b_res)

    plt.plot(*zip(*a_res), 'b')
    plt.plot(*zip(*b_res), 'r')
    plt.show()
    