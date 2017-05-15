import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12345)
x_list=np.array([0])
y_list=np.array([0])

for i in range(100000):
    theta=np.random.random()*2*np.pi
    addx=np.sin(theta)
    addy=np.cos(theta)
    new_x=x_list[-1]+addx
    new_y=y_list[-1]+addy
    x_list=np.append(x_list,new_x)
    y_list=np.append(y_list,new_y)
x_hist,x_edge=np.histogram(x_list,bins=10)
y_hist,y_edge=np.histogram(y_list,bins=10)
x_edge=(x_edge[1:]+x_edge[:-1])/2
y_edge=(y_edge[1:]+y_edge[:-1])/2

plt.figure()
plt.plot(x_list,y_list)
plt.show()
plt.figure()
plt.plot(x_edge,x_hist)
plt.plot(y_edge,y_hist)
plt.show()