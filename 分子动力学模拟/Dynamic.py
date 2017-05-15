import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation 
NP = 100
L = 100.0
kB = 1.0
T0 = 100.0
U0 = 1.0
epsilon = 1.0

dt = 0.1
time = 0.0
istep = 0

r2cut = (epsilon*2)**2
vcut = L/50/dt
tcouple = dt
rx = np.random.random(NP)*L
ry = np.random.random(NP)*L
vx = np.random.random(NP)
vy = np.random.random(NP)
T_list = np.zeros(300)
i_list = np.arange(300)
def force():
    global rx,ry,vx,vy,fx,fy,T,r2cut,xi
    fx = np.zeros(NP)
    fy = np.zeros(NP)
    for i in range(NP-1):
        for j in range(i+1,NP):
            dx = rx[i]-rx[j]
            dy = ry[i]-ry[j]
            dr2 = dx**2+dy**2
            if dr2 > r2cut:
                continue
            dr6 = dr2**3
            dr12 =dr2**6
            fc = (12.0*epsilon**12/dr12-6.0*epsilon**6/dr6)/dr2
            fx1 = fc*dx
            fy1 = fc*dy
            fx[i] += fx1
            fy[i] += fy1
            fx[j] -= fx1
            fy[j] -= fy1
    return
def mdrun():
    global rx, ry, vx, vy, vcut, fx, fy, T0, T, dt, time, istep,i_list,T_list
    force()
    vx += dt*fx
    vy += dt*fy
    for i in range(NP):
        if abs(vx[i]) > vcut:
            vx[i] = abs(vx[i])/vx[i]*vcut
        if abs(vy[i]) > vcut:
            vy[i] = abs(vy[i])/vy[i]*vcut
    rx += vx*dt
    ry += vy*dt
    v2 = np.sum(vx*vx)+np.sum(vy*vy)
    T = 0.5*v2/NP
    lamda = np.sqrt(1.0+dt/tcouple*(T0/T-1.0))
    vx *= lamda
    vy *= lamda
    for i in range(NP):
        if rx[i]<0 or rx[i]>L:
            vx[i] = -vx[i]
        if ry[i]<0 or ry[i]>L:
            vy[i] = -vy[i]
    istep += 1
    time = time + dt
    T_list[istep] = T
    return
def animate(i):
    mdrun()
    line.set_data(rx,ry)
    temp.set_data(i_list,T_list)
    return line
    return temp
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,xlim=(0,int(L)),ylim=(0,int(L)))
ax2 = fig.add_axes([0.6,0.2,0.25,0.25],ylim = (0,170))
line, = ax1.plot(rx,ry,'ro')
temp, = ax2.plot(i_list,T_list)
anim1 = animation.FuncAnimation(fig,animate,frames=1000,interval=1)
plt.show()

