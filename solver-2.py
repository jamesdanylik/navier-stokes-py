#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as aplt

nx = 41
dx = 10./(nx-1)
nt = 20
dt = .025
u = np.ones(nx)
u[.5/dx : 1/dx+1]=2
un = np.ones(nx)
c = .2


def init():
	line.set_data([], [])
	return line,



#plt.plot(np.linspace(0,2,nx), u)
#plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(0, 5))
line, = ax.plot([],[],lw=2)


def animate(i):
	print(i)
	un[:] = u[:]
	for i in range(1,nx):
		u[i] = un[i] - c*dt/dx*(un[i]-un[i-1])
	x = np.linspace(0,2,nx)
	#y = np.sin(2 * np.pi * (x - 0.01 * i))
	y = u
	line.set_data(x,y)
	return line,

anim = aplt.FuncAnimation(fig, animate, init_func=init,
                          frames=20, interval=50, blit=True)

# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec','libx264'])
plt.show()
