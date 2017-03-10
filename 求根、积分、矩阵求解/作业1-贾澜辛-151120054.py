import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
@jit
def f(theta,x0,y0):                                              #定义被积函数
    y=1/(np.sqrt((x0-np.cos(theta))**2+(y0-np.sin(theta))**2))
    return y
@jit
def V(x0,y0):                                                    #用辛普生公式求积分
    theta_list=np.linspace(0,2*np.pi,1001)
    v=0
    for i in range(1,1001,2):
       v += (f(theta_list[i-1],x0,y0)+4*f(theta_list[i],x0,y0)+f(theta_list[i+1],x0,y0))/(3*1000) 
    return v
fig =plt.figure()
ax=Axes3D(fig)                                                   #生成z轴并设置参数
ax.set_zlim(0,1.2)
X0=np.linspace(-1.1,1.1,100)                                     #生成xy平面并栅格化
Y0=np.linspace(-1.1,1.1,100)
X,Y=np.meshgrid(X0,Y0)
Z=V(X,Y)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'),vmax=2)   #绘制二维曲面图
ax.contourf(X,Y,Z,zdir='z',offset=0,cmap=plt.get_cmap('rainbow'))                #绘制等高线投影
plt.show()

