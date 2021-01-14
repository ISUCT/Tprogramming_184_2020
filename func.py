import math

def calc(a, b, x):
    num = pow(a,1/3)+pow(math.tan(b*x),4.5)
    denum = pow(b,1/5)+pow(1/math.tan(a*x),2.7)
    y = num/denum
    return y

a = 0.1
b = 0.5
x = 0.33
y = calc(a,b,x)

print (f"x={x} y={y}")