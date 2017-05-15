import numpy as np
import matplotlib.pyplot as plt
f1=lambda x,y:0.05*x
g1=lambda x,y:0.6*y
f2=lambda x,y:0.05*x
g2=lambda x,y:-0.5*x+1.0
f3=lambda x,y:0.46*x-0.32*y
g3=lambda x,y:0.39*x+0.38*y+0.6
f4=lambda x,y:0.47*x-0.15*y
g4=lambda x,y:0.17*x+0.42*y+1.1
f5=lambda x,y:0.43*x+0.28*y
g5=lambda x,y:-0.25*x+0.45*y+1.0
x_list=np.array([0.5])
y_list=np.array([0])
for i in range(10000):
    np.random.seed()
    a=np.random.random(100)
    for j in range(100):
        if a[j]<=0.1:
            x_list=np.append(x_list,f1(x_list[-1],y_list[-1]))
            y_list=np.append(y_list,g1(x_list[-1],y_list[-1]))
        elif 0.1<a[j]<=0.2:
            x_list=np.append(x_list,f2(x_list[-1],y_list[-1]))
            y_list=np.append(y_list,g2(x_list[-1],y_list[-1]))
        elif 0.2<a[j]<=0.4:
            x_list=np.append(x_list,f3(x_list[-1],y_list[-1]))
            y_list=np.append(y_list,g3(x_list[-1],y_list[-1]))
        elif 0.4<a[j]<=0.6:
            x_list=np.append(x_list,f4(x_list[-1],y_list[-1]))
            y_list=np.append(y_list,g4(x_list[-1],y_list[-1]))
        else:
            x_list=np.append(x_list,f5(x_list[-1],y_list[-1]))
            y_list=np.append(y_list,g5(x_list[-1],y_list[-1]))
plt.figure()
plt.scatter(x_list,y_list,s=1)
plt.show()