
import numpy as np
import matplotlib.pyplot as plt
AA = 0.0
BB = 20.0
ff = lambda x:x**4*np.exp(-x)
wt1 = lambda x:1.0/(BB-AA)
wt2 = lambda x:np.exp(-x)
wt3 = lambda x:x**3*np.exp(-x)/6.0
wt4 = lambda x:x**4*np.exp(-x)/24.0

max1 = 0.2
max2 = 1.0
max3 = 0.3
max4 = 0.3


list=np.array([])
ic=0
nt=1000
while ic<nt:
    a = np.random.random_sample()*(BB-AA)
    b = np.random.random_sample()*max3
    if b<=wt3(a):
        list = np.append(list,a)
        ic = ic+1
    else:
        pass


ll = 0.0
for i in range(len(list)):
    x = list[i]
    ll += ff(x)/wt3(x)
ll /= len(list)
print('the integral result is:%f'%ll)