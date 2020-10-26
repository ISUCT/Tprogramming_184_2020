import math

def calc(a, b, x):
    numerator = math.log((b**2 - x**2) ,a)
    denomerator = abs((x**2 - a**2))**(1/3.0)
    y = numerator/denomerator
    return y

def task_a(a, b, xn, xk, dx):
    x = xn
    y = []
    while x <= xk:
        res = calc(a, b, x)
        y.append(res)
        x += dx
    return y

def task_b(a, b, x_arr):
    y = []
    for x in x_arr:
        res = calc(a, b, x)
        y.append(res)
    return y

if __name__ == "__main__":
    a = 2.0
    b = 4.1
    x = 0.77
    y = calc(a, b, x)
    print(f"x={x:.3f} y={y:.3f}")

    a_res = task_a(a, b, 0.77, 1.77, 0.2)
    print(a_res)

    x_arr = [1.24, 1.38, 2.38, 3.21, 0.68]
    b_res = task_b(a, b, x_arr)
    print(b_res)



