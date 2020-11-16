import numpy as np
import matplotlib.pyplot as plt
import math

def calc(a, b, x):
    numerator = a * math.sqrt(x) - b * math.log(x,5)
    denomerator = math.log10(abs(x-1))
    y = numerator/denomerator
    return y

def calc_np(a, b, x):
    numerator = a * math.sqrt(x) - b * math.log(x,5)
    denomerator = math.log10(abs(x-1))
    y = numerator/denomerator
    return y

def task_a_np(a, b, xn, xk, dx):
    x = np.arange(xn, xk, dx)
    y = calc_np(a, b, x)
    return x, y

def task_a(a, b, xn, xk, dx):
    i = xn
    
    res = []
    while i <= xk:
        y = calc(a, b, i)
        res.append((i, y))
        i += dx
    return res

def task_b(a, b, x_arr):
    y = []
    for x in x_arr:
        res = calc(a, b, x)
        y.append(res)
    return y

def draw(x, y):
    fig = plt.plot(x, y, 'rx')
    fig[0].figure.add_axes(xlabel="asdfasdf")
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("My graphics")
    plt.show()

if __name__ == "__main__":
    a = 4.1
    b = 2.7
    x = 1.2
    y = calc(a, b, x)
    print(f"x={x:.3f} y={y:.3f}")


    x, y = task_a_np(a, b, 1.2, 5.2, 0.8)
    draw(x, y)
    # print(a_res)

    x_arr = [1.9, 2.15, 2.34, 2.73, 3.16]
    b_res = task_b(a, b, x_arr)
    print(b_res)
