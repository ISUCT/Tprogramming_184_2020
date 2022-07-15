from math import log10
import matplotlib.pyplot as plt
import numpy as np


def calc(a, x):
    t = x ** 2 - 1
    y = a ** t - log10(t) + t ** (1 / 3)
    return y


def func(a, X):
    Y = list()
    for elem in X:
        res = calc(a, elem)
        Y.append(res)
    return Y


if __name__ == '__main__':
    a = 2.25
    x_beg = 1.2
    x_end = 2.7
    x_del = 0.3
    fig, axs = plt.subplots(1, 2, figsize=(8, 4))

    X = np.arange(x_beg, x_end, x_del)
    Y = func(a, X)
    axs[0].plot(X, Y)
    axs[0].grid()
    axs[0].set(xlabel='Параметр A', ylabel='Функция A', title='График A')

    X = [1.31, 1.39, 1.44, 1.56, 1.92]
    Y = func(a, X)
    axs[1].plot(X, Y)
    axs[1].grid()
    axs[1].set(xlabel='Параметр B', ylabel='Функция B', title='График B')

    fig.savefig("Graph.png")
    plt.show()
