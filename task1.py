import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.01)

def diff_func(w, x) :
    y, z = w
    dy_dx = y**2*z
    dz_dx = (z/x) - y*(z**2)
    return dy_dx, dz_dx

y0 = 1
z0 = -3
w = y0, z0

sol = odeint(diff_func,w,x)


	
plt.plot(x, sol[:, 0], 'b', label='theta(t)')
plt.savefig('fig_3.png')