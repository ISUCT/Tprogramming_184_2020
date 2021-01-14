import math
import matplotlib.pyplot as plt
import numpy as np

def calc_np(a, b, x):
    num = a**1/3+pow(np.tan(b*x),4.5)
    denum = b**1/5+pow(1/np.tan(a*x),2.7)
    y = num/denum
    return y

def task_b(a, b, x_arr):
    y = []
    for x in x_arr:
        res = calc_np(a, b, x)
        y.append(res)
    return y

def draw(xs, ys):
    fig = plt.subplots()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("My graphics")
    plt.plot(xs,ys)
    plt.show()


a = 0.1
b = 0.5
xn = 0.33
xk = 1.23
dx = 0.18
x_arr = [0.5, 0.36, 0.40, 0.62, 0.78]
y = [task_b(a,b, x_arr)]

xs = []
ys = []

while xn<=xk:
    y = calc_np(a, b, xn)
    xs.append(xn)
    ys.append(y)
    xn+=dx

print()
print(f"Task A: x={xs} y={ys}")
print()
print(f"Task B: x1={x_arr} y1={y}")
draw(xs, ys)