import math

def calc(a, b, x):
    num = pow(a,1/3)+pow(math.tan(b*x),4.5)
    denum = pow(b,1/5)+pow(1/math.tan(a*x),2.7)
    y = num/denum
    return y

a = 0.1
b = 0.5
x = 0.33
x1 = 1.23
dx = 0.18
xs = []
ys = []

while x<=x1:
    y = calc(a,b,x)
    xs.append(x)
    ys.append(y)
    x+=dx

print (f"x={xs} y={ys}")