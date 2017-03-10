import numpy as np
from numba import jit
@jit
def f(x):
   y=np.exp(x)*np.log(x)-x**2
   return y
a_list=np.array([1])
b_list=np.array([2])
for i in range(100):
    c=(a_list[-1]+b_list[-1])/2
    if f(a_list[-1])*f(c)<0:
        b_list=np.append(b_list,c)
    else:
        a_list=np.append(a_list,c)
    if i%10==0:
        print(c)