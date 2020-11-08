from math import log
import matplotlib.pyplot as graph_task_a
import matplotlib.pyplot as graph_task_b
import numpy as np

def calc(a, x):
    t = pow(x, 2) - 1
    y = pow(a, t) - log(t, 10) + pow(t, (1 / 3))
    return y

def task_a(a, xn, xk, dx):
    x = xn
    x_arr = list()
    y = list()
    while x <= xk:
        res = calc(a, x)
        y.append(res)
        x_arr.append(x)
        x += dx
    return y, x_arr

def task_b(a, x_arr):
    y = list()
    for x in x_arr:
        res = calc(a, x)
        y.append(res)
    return y

if __name__ == '__main__':
    a = 2.25
    xn = 1.2
    xk = 2.7
    dx = 0.3

    a_res, x_arr_task_a = task_a(a, xn, xk, dx)

    x_arr_task_b = [1.31, 1.39, 1.44, 1.56, 1.92]

    b_res = task_b(a, x_arr_task_b)

    print(a_res)
    print(x_arr_task_a)
    print(b_res)
    print(x_arr_task_b)

    fig1, ax1 = graph_task_a.subplots()
    fig2, ax2 = graph_task_b.subplots()

    ax1.set(xlabel = 'Parameter_a', ylabel = 'Value_a', title = 'task_a')
    ax2.set(xlabel = 'Parameter_b', ylabel = 'Value_b', title = 'task_b')
    
    ax1.grid()
    ax2.grid()

    ax1.plot(x_arr_task_a, a_res)
    ax2.plot(x_arr_task_b, b_res)

    fig1.savefig('task_a.png')
    fig2.savefig('task_b.png')

    graph_task_a.show()
    graph_task_b.show()