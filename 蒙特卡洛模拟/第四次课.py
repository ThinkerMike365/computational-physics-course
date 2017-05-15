import numpy as np
import matplotlib.pyplot as plt

def potential(x):
    if x < -5:
        y = (x+5)**2
    elif x < 0:
        y = 0
    elif x == 0:
        y = 10 
    elif x < 5:
        y = 0
    else:
        y = (x-5)**2
    return y

R = 8.3
RT = R*0.1
Einc = 0.1
H = np.zeros(2*xmax+1)
xp, ee = metadync(RT, Einc, 1800)

Einc = 0.0
xp ,ee = metadync(RT, Einc,10000)

def metadync(RT,Einc,nstep):
    x = 1
    E = potential(x)+H[x]
    xx = [] 
    ee = []
    for istep in range(nstep):
        if np.random.random_sample() < 0.5:
            xnew = x+1
        else:
            xnew = x-1
        Enew = potential(xnew)+H[xnew]
        if Enew <= E:
            x = xnew
            E = Enew
        else:
            w = np.exp(-(Enew-E)/RT)
            if np.random.random_sample() < w:
                x = xnew
                E = Enew
        H[x] += Einc
        xx.append(x)
        ee.append(E)
    return xx, ee
Xavg = 0.0
Wsum = 0.0
for i in range(len(xp)):
    x = xp[i]
    E = potential(x)
    W = np.exp((H[x]-E)/RT)
    Wsum += W
    Xavg += 