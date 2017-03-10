import numpy as np
from numba import jit
import matplotlib.pyplot as plt
@jit
def V(x0,y0):
    x_=np.linspace(-10,10,501)
    v=0
    for i in range(1,501,2):
        v=v+ (f(x_[i-1],x0,y0)+4*f(x_[i],x0,y0)+f(x_[i+1],x0,y0))*20/1500
    return v
@jit
def f(x,x0,y0):
    y=1/np.sqrt((x-x0)**2+y0**2)
    return y
X0=np.linspace(-11,11,500)
Y0=np.linspace(-11,11,500)
X,Y=np.meshgrid(X0,Y0)
plt.figure()
plt.contourf(X,Y,V(X,Y),8,alpha=0.75,cmap=plt.get_cmap('rainbow'))
C=plt.contour(X,Y,V(X,Y),8,colors='black',linewidth=.1)
plt.clabel(C,inline=True,fontsize=5)
plt.xticks(())
plt.yticks(())
plt.show()
    