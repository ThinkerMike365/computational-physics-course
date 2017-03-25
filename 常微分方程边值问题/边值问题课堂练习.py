import numpy as np
import matplotlib.pyplot as plt 
gg=10.0
def derv_f(y1,y2,x):
    gamma=0.01
    s=-gg-gamma*y1
    return s
def derv_g(y1,y2,x):
    s=y1
    return s
def Runge_Kutta(x,y1,y2,h):
    y1half=y1+derv_f(y1,y2,x)*h*0.5
    y2half=y2+derv_g(y1,y2,x)*h*0.5
    y1next=y1+derv_f(y1half,y2half,x+0.5*h)*h
    y2next=y2+derv_g(y1half,y2half,x+0.5*h)*h
    return (y1next,y2next)
def Integeral(xx,y1,y2,N,h):
    for i in range(N):
        y1[i+1],y2[i+1]=Runge_Kutta(xx[i],y1[i],y2[i],h)
    return
xa=0.0
xb=5.0
N=100
h=(xb-xa)/N
xx=np.linspace(xa,xb,N+1,dtype=np.float64)
y1=np.zeros(N+1,dtype=np.float64)
y2=np.zeros(N+1,dtype=np.float64)
y2[0]=0.0
y1[0]=30.0
loss=(y2[-1]-40)**2
addx=1.0
Integeral(xx,y1,y2,N,h)
print(y2[-1])
y1[0]=31
oldy2_list=np.array([y2[-1]])
while loss>=0.000001:
    oldy2=oldy2_list[-1]-40
    Integeral(xx,y1,y2,N,h)
    recenty2=y2[-1]-40
    if oldy2*recenty2>0:
        y1[0]=y1[0]+addx
        oldy2_list=np.append(oldy2_list,y2[-1]-40)
    else:
        addx=addx/2
        y1[0]=y1[0]-addx
    loss=(y2[-1]-40)**2
    print(y1[0])     
plt.figure()
plt.plot(xx,y2)
plt.plot(xx,y1)
plt.show()