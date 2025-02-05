import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5,5,0.01)

def diff_func(w,t):
    y,v  = w
    dy_dt = v 
    dv_dt = -4*v - 5*y
    return dy_dt, dv_dt

y0 = 4
v0 = -1
w0 = y0,v0


sol = odeint(diff_func,w0,t)


	
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.savefig('fig_6.png')