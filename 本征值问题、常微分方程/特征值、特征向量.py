import numpy as np
import matplotlib.pyplot as plt
A=np.array([[4,2,2 ],[2,5,1],[2,1,6]])
eigenValues,eigenVectors=np.linalg.eig(A)
print('eigen Values',eigenValues)
print('eigen Vectors',eigenVectors)
n=3
plt.plot(range(n),eigenValues,'ro')
plt.show()
plt.plot(range(n),eigenVectors[:,0],'ro')
plt.show()
