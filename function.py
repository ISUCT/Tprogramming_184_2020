import numpy as np
import matplotlib.pyplot as plt
# import math

def calc(a, b, x):
     if (x < 5):
        numerator = np.pow(np.log10(np.pow(a, 2) + x), 2)
        denominator = np.pow(a + x, 2)
        y = numerator / denominator
        return y
     else: 
        numerator = np.pow(a + (b * x), 2.5)
        denominator = 1.8 + np.pow(np.cos(a * x), 3)
        y = numerator / denominator
        return y

def calc_np(a, b, x):
     if (x < 5):
        numerator = np.pow(np.log(np.pow(a, 2) + x), 2)/np.log(10)
        denominator = np.pow(a + x, 2)
        y = numerator / denominator
        return y
     else:
        numerator = np.pow(a + (b * x), 2.5)
        denominator = 1.8 + np.pow(np.cos(a * x), 3)
        y = numerator / denominator
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
    a = -2.5
    b = 3.4
    x = 3.5
    # y = calc(a, b, x)
    # print(f"x={x:.3f} y={y:.3f}")


    x, y = task_a_np(a, b, 3.5, 6.5, 0.6)
    draw(x, y)
    # print(a_res)

    # x_arr = [2.89, 3.54, 5.21, 6.28, 3.48]
    # b_res = task_b(a, b, x_arr)
    # print(b_res)