import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit
t1=time.time()
#定义算法
#@jit
def interpolate(x_test,x_train,y_train):
    n_x=x_train.shape[0]
    n_y=y_train.shape[0]
    y_predict=np.array([])
    for m in x_test:
        if n_x != n_y:
            print('x,y do not have the same lenth')
        else:  
            A_list=np.array([])
            for j in range(n_x):
                A_j = 1
                A_ij = 0
                for i in range(n_x):
                    if i == j:
                        continue
                    else:
                        A_ij = (m-x[i])/(x[j]-x[i])
                        A_j=A_j*A_ij
                A_list=np.append(A_list,A_j)
        y_predict=np.append(y_predict,np.dot(A_list,y))
    return y_predict
#定义所用的函数
@jit
def function(a):
    return 1/(a**2+1)
#构造数据点
x=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
y=np.array([])
for i in range(11):
    y=np.append(y,function(x[i]))
#计算插值函数和原函数本身
x_axis=np.linspace(-6,6,1000)
y_new=interpolate(x_axis,x,y)
y_origin=function(x_axis)
##绘图
plt.figure()
##绘制数据点
plt.scatter(x,y)
##绘制插值曲线并加标识
plt.plot(x_axis,y_new,label=r'$interpolate\ curve$')
plt.annotate(r'$y=\frac{1}{1+x^2}$',xy=(2.5,function(2.5)),xycoords='data',xytext=(+20,+20),textcoords='offset points',fontsize=12,arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=0.5"))
##绘制原函数并加标识
plt.plot(x_axis,y_origin,label=r'$function\ curve$')
plt.annotate(r'$10-Order\ Lagrange$',xy=(-2.5,interpolate([-2.5],x,y)),xycoords='data',xytext=(-10,-50),textcoords='offset points',fontsize=10,arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
##加显示范围和标签
plt.ylim(-1,1.5)
plt.legend()  
plt.show()
t2=time.time()
print(t2-t1)

    

    

    
