import numpy as np
import matplotlib.pyplot as plt
from numba import jit 
from mpl_toolkits.mplot3d import Axes3D
sigma=10
b=8/3
r=25
@jit
def f(x1,y1,z1,t1):
    return sigma*(y1-x1)
@jit
def g(x2,y2,z2,t2):
    return -x2*z2+r*x2-y2
@jit
def h(x3,y3,z3,t3):
    return x3*y3-b*z3
x_list=np.array([1])
y_list=np.array([1])
z_list=np.array([1])
t_list=np.array([0])
delta_t=0.001
for i in range(100000):
    t_n=t_list[-1]
    x_n=x_list[-1]
    y_n=y_list[-1]
    z_n=z_list[-1]
    k1=f(x_n,y_n,z_n,t_n)
    l1=g(x_n,y_n,z_n,t_n)
    m1=h(x_n,y_n,z_n,t_n)
    x_nplusahalf=x_n+k1*delta_t/2
    y_nplusahalf=y_n+l1*delta_t/2
    z_nplusahalf=z_n+m1*delta_t/2
    t_nplusahalf=t_n+delta_t/2
    k2=f(x_nplusahalf,y_nplusahalf,z_nplusahalf,t_nplusahalf)
    l2=g(x_nplusahalf,y_nplusahalf,z_nplusahalf,t_nplusahalf)
    m2=h(x_nplusahalf,y_nplusahalf,z_nplusahalf,t_nplusahalf)
    x_nplusahalf=x_n+k2*delta_t/2
    y_nplusahalf=y_n+l2*delta_t/2
    z_nplusahalf=z_n+m2*delta_t/2
    t_nplusahalf=t_n+delta_t/2
    k3=f(x_nplusahalf,y_nplusahalf,z_nplusahalf,t_nplusahalf)
    l3=g(x_nplusahalf,y_nplusahalf,z_nplusahalf,t_nplusahalf)
    m3=h(x_nplusahalf,y_nplusahalf,z_nplusahalf,t_nplusahalf)
    x_nplusone=x_n+k3*delta_t
    y_nplusone=y_n+l3*delta_t
    z_nplusone=z_n+m3*delta_t
    t_nplusone=t_n+delta_t
    k4=f(x_nplusone,y_nplusone,z_nplusone,t_nplusone)
    l4=g(x_nplusone,y_nplusone,z_nplusone,t_nplusone)
    m4=h(x_nplusone,y_nplusone,z_nplusone,t_nplusone)
    new_x=x_n+(k1+2*k2+2*k3+k4)*delta_t/6
    new_y=y_n+(l1+2*l2+2*l3+l4)*delta_t/6
    new_z=z_n+(m1+2*m2+2*m3+m4)*delta_t/6
    new_t=t_n+delta_t
    x_list=np.append(x_list,new_x)
    y_list=np.append(y_list,new_y)
    z_list=np.append(z_list,new_z)
    t_list=np.append(t_list,new_t)
fig=plt.figure()
ax=Axes3D(fig)
ax.plot3D(x_list,y_list,z_list,linewidth=0.5)
plt.show()
