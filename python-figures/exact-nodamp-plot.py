# Based on https://kitchingroup.cheme.cmu.edu/blog/2013/02/21/Phase-portraits-of-a-system-of-ODEs/

# Importing mathematics packages.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)

# Plot settings.
figure = plt.figure(figsize=(8, 4), dpi=400)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\frac{d\theta}{dt}$')
plt.xlim([-(5/2)*np.pi, (5/2)*np.pi])
plt.ylim([-3.5, 3.5])
plt.xticks(np.arange(-2*np.pi, 2*np.pi+np.pi, step=(np.pi)), [r'$-2\pi$',r'$-\pi$',r'0',r'$\pi$',r'$2\pi$'])

q = 0 # Friction coefficient.
t = 0 # Time.
m = 1 # Mass.
g = 10 # Gravitational acceleration.
L = 10 # Length.

# Definition of ODE separated in outputs.
def f(Y, t):
    y1, y2 = Y
    return [y2, -(g/L)*np.sin(y1)-(q/m)*y2]

#
# Creating phase picture as vector map.
#

# Input values for the function.
xin = np.linspace(-3*np.pi, 3*np.pi, 28)
yin = np.linspace(-3.5, 3.5, 20)
Y1, Y2 = np.meshgrid(xin, yin) # Combining input values in an array.

u, v = np.zeros(Y1.shape), np.zeros(Y2.shape) # Defining empty vector arrays for horizontal and vertical components.

# Cycling through every pair of inputs, calculating the output vectors for each and storing them in the empty vector arrays.
NI, NJ = Y1.shape 
for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        dy = f([x, y], t)
        u[i,j] = dy[0]
        v[i,j] = dy[1]

mag = np.sqrt(u*u+v*v) # Calculating magnitude of vectors for color map.
Q = plt.quiver(Y1, Y2, u, v, mag, cmap=plt.cm.jet) # Plotting vector map.
plt.plot([-2*np.pi, 0, 2*np.pi], [0, 0, 0], 'bo', markersize=4, label=r'Stable points') # Plotting attractor points.
plt.plot([-np.pi, np.pi], [0, 0], 'ro', markersize=4, label=r'Unstable points') # Plotting unstable points.
plt.legend(labelcolor='linecolor', fancybox=False, facecolor='white', edgecolor='black', framealpha=1, loc='upper right') # Legend settings.

plt.savefig('/home/pedro/Desktop/IA\'/phase_exact_simple_noplot.svg', dpi=400, facecolor='w', edgecolor='w') # Saving figure.