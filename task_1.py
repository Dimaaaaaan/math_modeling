import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,240,0.01)
N = 1
k = 1/15
def radio_function(N,t):
    dmdt = k*N
    return dmdt

N_t = odeint(radio_function, N, t)

plt.plot(t, N_t[:,0])
plt.savefig("fig_2.png")