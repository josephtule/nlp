def c(x):
    return x**2 + 2*x + 1

def secant(c,x,xkm1):
    return (c(x) - c(xkm1))/(x-xkm1)

x0 = 3
xkm1 = 2*x0
x = x0

err = 1000
i = 1
while (err > 1e-10):
    xkp1 = x - c(x)/secant(c,x,xkm1)
    err = abs(x - xkp1)
    i = i+1
    print(err)
    x = xkp1
print(x)
print(i)
