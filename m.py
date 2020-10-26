import math
def calc(a, b, x):
    numerator = math.asin(math.pow(x,a))-math.acos(math.pow(x,b))
    return numerator

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
    a = 2
    b = 3
    x = 0.11
    y = calc(a, b, x)
    print(f'x={x:.3f} y={y:.3f}')

    a_res = task_a(a, b, 0.11, 0.36, 0.05)
    print(a_res)

    x_arr = [0.08, 0.26, 0.35, 0.41, 0.53]
    b_res = task_b(a, b, x_arr)
    print(b_res)