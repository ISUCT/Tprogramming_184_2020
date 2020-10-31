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
    a = -2.5
    b = 3.4
    x = 3.5
    y = calc(a, b, x)
    print(f'x={x:.3f} y={y:.3f}')

    a_res = task_a(a, b, 3.5, 6.5, 0.6)
    print(a_res)

    x_arr = [2.89, 3.54, 5.21, 6.28, 3.48]
    b_res = task_b(a, b, x_arr)
    print(b_res)
    