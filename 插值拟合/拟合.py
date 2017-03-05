import numpy as np
import matplotlib.pyplot as plt
p=np.array([36.9,46.7,63.7,77.8,84.0,87.5])
delta=np.array([181,197,235,270,283,292])
delta_fit=np.poly1d(np.polyfit(p,delta,1))
p_axis=np.linspace(30,90,100)
plt.figure()
plt.plot(p,delta,'.',p_axis,delta_fit(p_axis),'-')
plt.show()