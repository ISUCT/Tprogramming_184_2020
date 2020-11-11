import matplotlib.pyplot as plt
import math

def calc(x):
    y = (abs(x**2 - 2.5))**(1/4.0) + (math.log10(x**2))**(1/3.0)
    return y

def task_a(xn, xk, dx):
    
    x = xn
    res = []

    while x <= xk:
        y = calc(x)
        res.append((x, y))
        x += dx

    return res

def task_b(x_list):
    
    res = []
    for x in x_list:
        y = calc(x)
        res.append((x, y))

    return res

if __name__ == "__main__":

    # Task A
    result_a = task_a(1.25, 3.25, 0.4)
    formatted_list_a = ['%.2f' % x[0] for x in result_a]
    print(*formatted_list_a, sep=", ")

    # Task B
    x_list = [1.84, 2.71, 3.81, 4.56, 5.62]
    result_b = task_b(x_list)
    formatted_list_b = ['%.2f' % x[0] for x in result_b]
    print(*formatted_list_b, sep=", ")

    plt.plot(*zip(*result_a), 'b')
    plt.plot(*zip(*result_b), 'r')
    plt.show() 