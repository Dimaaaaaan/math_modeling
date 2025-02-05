import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,8,0.1)
I = 1000
k = 0.08
def radio_function(I,t):
    dmdt = -k*I*t
    return dmdt

I_t = odeint(radio_function, I, t)

plt.plot(t, I_t[:,0])
plt.savefig("fig_3.png")