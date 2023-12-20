import numpy as np


def c(x):
    return 2*x**2 + 2*x - 1
def cp(x):
    return 4*x + 2

x0 = 1
x = x0
err = 1000
while (err > 1e-5):
    xk = x - c(x)/cp(x)
    err = abs(x - xk)
    x = xk
print(x)
