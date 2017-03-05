import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,np.pi,100)
y1=np.sin(x)
y2=np.exp(x)
y1d =np.array([])
y1d_=np.array([])
y2d=np.array([])
for i in range(99):
    d=(y1[i+1]-y1[i])/(np.pi/99)
    y1d =np.append(y1d,d)
for _ in range(1,99):
    d_=(y1[_+1]-y1[_-1])/(np.pi/49.5)
    y1d_=np.append(y1d_,d_)
plt.figure()
plt.plot(x,y1)
plt.plot(x[:-1],y1d)
plt.plot(x[1:-1],y1d_)
plt.show()
for j in range(99):
    d2=(y2[j+1]-y2[j])/(np.pi/99)
    y2d=np.append(y2d,d2)
plt.figure()
plt.plot(x,y2)
plt.plot(x[:-1],y2d)
plt.show()