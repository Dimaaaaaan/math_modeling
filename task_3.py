import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,8,0.1)
ao = 10 
U = 5
m = 100
y = 0.1
def radio_function(U,t):
    dmdt = ao - (y/m)*U**2
    return dmdt

U_t = odeint(radio_function, U, t)

plt.plot(t, U_t[:,0])
plt.savefig("fig_4.png")