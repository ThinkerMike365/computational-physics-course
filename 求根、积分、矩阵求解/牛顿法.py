import numpy as np
def f(x):
    y=np.exp(x)*np.log(x)-x**2
    return y
def f_prime(x):
    yd=np.exp(x)/x+np.exp(x)*np.log(x)-2*x
    return yd
x_list=np.array([1])
for i in range(10):
    newx=x_list[-1]-f(x_list[-1])/f_prime(x_list[-1])
    print(newx)
    x_list=np.append(x_list,newx)
