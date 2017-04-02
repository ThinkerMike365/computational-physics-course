import numpy as np
import matplotlib.pyplot as plt
f=lambda x:np.sin(2*np.pi*x)                                #定义函数
tao=0.005                                                   #选定参数
h=0.1
N=500
M=50
U=np.zeros([N+1,M+1])                                       #构建解空间
for i in range(M+1):                                        #在解空间写入初始条件
    U[0][i]=f(i*h)
    U[1][i]=f(i*h)
for k in range(1,N):                                        #计算
    for i in range(1,M):
        U[k+1][i]=2*(1-(tao/h)**2)*U[k][i]+(tao/h)**2*(U[k][i+1]+U[k][i-1])-U[k-1][i]
fig=plt.figure()                                            #绘图
ax1=fig.add_subplot(1,1,1)
levels=np.arange(-2.0,2.0,0.01)
ax1.contourf(U,levels,camp=plt.cm.hot)
plt.show()