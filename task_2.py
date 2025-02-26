import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


frames = 1000
seconds_in_year = 365*24*60*60
years = 1
	
t = np.linspace(0, years*seconds_in_year, frames)
	
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3,y3,v_y3,
     x4, v_x4,y4,v_y4,
     x5, v_x5,y5,v_y5,
     x6, v_x6,y6,v_y6,) = s
 
    dxdt1 = v_x1
    dv_xdt1 = (k/m) * (q1*Qx) / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = (k/m) * (q1*Qy) / (x1**2 + y1**2)**1.5
 
    dxdt2 = v_x2
    dv_xdt2 = (k/m) * (q2*Qx) / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = (k/m) * (q2*Qy) / (x2**2 + y2**2)**1.5

    dxdt3 = v_x3
    dv_xdt3 = (k/m) * (q3*Qx) / (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = (k/m) * (q3*Qy) / (x3**2 + y3**2)**1.5

    dxdt4 = v_x4
    dv_xdt4 = (k/m) * (q4*Qx) / (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = (k/m) * (q4*Qy) / (x4**2 + y4**2)**1.5

    dxdt5 = v_x5
    dv_xdt5 = (k/m) * (q5*Qx) / (x5**2 + y5**2)**1.5
    dydt5 = v_y5
    dv_ydt5 = (k/m) * (q5*Qy) / (x5**2 + y5**2)**1.5

    dxdt6 = v_x6
    dv_xdt6 = (k/m) * (q6*Qx) / (x6**2 + y6**2)**1.5
    dydt6 = v_y6
    dv_ydt6 = (k/m) * (q6*Qy) / (x6**2 + y6**2)**1.5
 
 
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3,dv_xdt3,dydt3,dv_ydt3,
            dxdt4,dv_xdt4,dydt4,dv_ydt4,
            dxdt5,dv_xdt5,dydt5,dv_ydt5,
            dxdt6,dv_xdt6,dydt6,dv_ydt6,)

k = 9 * 10**9
m = 0.1
Qx = 10
Qy = 5

q1,q2,q3 = 2,3,4
q4,q5,q6 = -2,-3,-4

	
x10 = 0
v_x10 = 0
y10 = 0.287 * 149 * 10**9
v_y10 = 300
 
x20 = 0
v_x20 = -473
y20 = 0.387 * 149 * 10**9
v_y20 = 0

x30 = 0
v_x30 = -400
y30 = 0.587 * 149 * 10**9
v_y30 = 0

x40 = 0
v_x40 = -500
y40 = 0.687 * 149 * 10**9
v_y40 = 0

x50 = 0
v_x50 = -600
y50 = 0.787 * 149 * 10**9
v_y50 = 0

x60 = 0
v_x60 = -700
y60 = 0.887 * 149 * 10**9
v_y60 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,)

sol = odeint(move_func, s0, t)

plt.plot([0], [0], 'o', color='y', ms=20)
	
fig, ax = plt.subplots()
 
ball1, = plt.plot([], [], 'o', color='r')
ball_line1, = plt.plot([], [], '-', color='r')

ball2, = plt.plot([], [], 'o', color='blue')
ball_line2, = plt.plot([], [], '-', color='blue')

ball3, = plt.plot([], [], 'o', color='green')
ball_line3, = plt.plot([], [], '-', color='green')

ball4, = plt.plot([], [], 'o', color='green')
ball_line4, = plt.plot([], [], '-', color='green')

ball5, = plt.plot([], [], 'o', color='green')
ball_line5, = plt.plot([], [], '-', color='green')

ball6, = plt.plot([], [], 'o', color='green')
ball_line6, = plt.plot([], [], '-', color='green')

 
def animate(i):
    ball1.set_data([sol[i][0]], [sol[i][2]])
    ball_line1.set_data(sol[:i, 0], sol[:i, 2])

    ball2.set_data([sol[i][4]], [sol[i][6]])
    ball_line2.set_data(sol[:i, 4], sol[:i, 6])

    ball3.set_data([sol[i][8]], [sol[i][10]])
    ball_line3.set_data(sol[:i, 8], sol[:i, 10])

    ball4.set_data([sol[i][12]], [sol[i][14]])
    ball_line4.set_data(sol[:i, 12], sol[:i, 14])

    ball5.set_data([sol[i][16]], [sol[i][18]])
    ball_line5.set_data(sol[:i, 16], sol[:i, 18])

    ball6.set_data([sol[i][20]], [sol[i][22]])
    ball_line6.set_data(sol[:i, 20], sol[:i, 22])


 
 
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
 
edge =  y60
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('equal')
	
ani.save('fig_3.gif')