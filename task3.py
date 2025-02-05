import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5,5,0.01)

def diff_func(w,t):
    y, v = w

    dy_dt = v
    dv_dt = np.sin(t) + np.cos(t)
    
    return dy_dt, dv_dt

y0 = 0 
v0 = 3
w0 = y0, v0


sol = odeint(diff_func,w0,t)


	
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.savefig('fig_5.png')