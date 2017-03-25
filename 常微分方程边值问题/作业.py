import numpy as np
import matplotlib.pyplot as plt
derv_phi = lambda phi, y, x, k:y
derv_y = lambda phi, y, x, k: -k**2*phi
def Runge_Kutta(x, phi, y, k, h):
    phihalf = phi+derv_phi(phi, y, x, k)*h*0.5
    yhalf = y+derv_y(phi, y, x, k)*h*0.5
    phinext = phi+derv_phi(phihalf, yhalf, x+0.5*h, k)*h
    ynext = y+derv_y(phihalf, yhalf, x+0.5*h, k)*h
    return (phinext, ynext)
def Integral(xx, phi_list, y_list, N, h, k):
    for i in range(N):
        phi_list[i+1], y_list[i+1] = Runge_Kutta(xx[i], phi_list[i], y_list[i], k, h)
    return
xa = 0.0
xb = 1.0
N = 100
h = (xb-xa)/N
xx = np.linspace(xa, xb, N+1, dtype=np.float64)
phi_list = np.zeros(N+1, dtype=np.float64)
y_list = np.zeros(N+1, dtype=np.float64)
y_list[0] = 10
phi_list[0] = 0
k = 8
addk = 0.1
Integral(xx, phi_list, y_list, N, h, k)
k = k+addk
loss = (phi_list[-1])**2
oldphi_list = np.array([phi_list[-1]])
while loss>=0.00000000001:
    oldphi = oldphi_list[-1]
    Integral(xx,phi_list,y_list,N,h,k)
    recentphi = phi_list[-1]
    if oldphi*recentphi>0:
        k = k+addk
        oldphi_list = np.append(oldphi_list,recentphi)
    else:
        addk = addk/2
        k = k-addk
    loss = (phi_list[-1])**2
    print(k)
plt.figure()
plt.plot(xx, phi_list)
plt.show()

