import numpy as np
import matplotlib.pyplot as plt
def interpolate(x_test,x_train,y_train):
    n_x=len(x_train)
    n_y=len(y_train)
    y_predict=np.array([])
    for m in x_test:
        if n_x != n_y:
            print('x,y do not have the same lenth')
        else:  
            j=0
            A_list=np.array([])
            while j < n_x:
                i=0
                A_j = 1
                A_ij = 0
                while i < n_x:
                    i=i+1
                    if i-1 == j:
                        continue
                    else:
                        A_ij = (m-x[i-1])/(x[j]-x[i-1])
                        A_j=A_j*A_ij
                A_list=np.append(A_list,A_j)
                j = j+1
        y_predict=np.append(y_predict,np.dot(A_list,y))
    return y_predict
x_new=np.linspace(0,3500,10000)
x=np.array([324,855,1721,2190,2501,3086])
y=np.array([846.8,1037.8,1238.3,1771.4,2034.0,2598.5])
plt.figure()
plt.plot(x_new,interpolate(x_new,x,y))
plt.show()                    