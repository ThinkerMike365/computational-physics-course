import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as am
NP = 100
x = np.random.random(NP)
y = np.random.random(NP)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, xlim=(0, 1), ylim=(0, 1))
line, = ax1.plot(x, y, 'ro')
def animate(i):
    global x, y
    vx = np.random.random(NP)
    vy = np.random.random(NP)
    x = x + vx
    y = y + vy
    line.set_data(x, y)
    return line
anim1 = am.FuncAnimation(fig, animate, frames=100, interval=10)
plt.show()