import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
x_new=np.linspace(0,3500,10000)
x=np.array([324,855,1721,2190,2501,3086])
y=np.array([846.8,1037.8,1238.3,1771.4,2034.0,2598.5])
f=interpolate.lagrange(x,y)
y_new=f(x_new)
g=interpolate.splrep(x,y,k=3)
y_new2=interpolate.splev(x_new,g)
plt.figure()
p1=plt.plot(x_new,y_new,label='拉格朗日插值')
p2=plt.plot(x_new,y_new2,label='样条插值')
plt.legend()
plt.scatter(x,y)
plt.show()