#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt #
import time, sys
from IPython.core.display import clear_output

nx = 41
dx = 2./(nx-1)
nt = 25
dt = .025
c = 1.

u = np.ones(nx)
u[.5/dx : 1/dx+1]=2
print(u)

# plt.plot(np.linspace(0,2,nx), u)
# plt.show()

un = np.ones(nx)
for n in range(nt):
	un[:] = u[:]
	for i in range(1,nx):
		u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])

plt.plot(np.linspace(0,2,nx), u)
plt.show()
