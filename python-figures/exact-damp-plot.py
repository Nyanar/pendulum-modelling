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

q = 0.2 # Friction coefficient.
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
plt.plot([-2*np.pi, 0, 2*np.pi], [0, 0, 0], 'bo', markersize=4) # Plotting attractor points.

#
# Plotting some solutions of the differential equation.
#

# Importing package 'odeint' which calculates solutions of ODEs.
from scipy.integrate import odeint

# Plot settings.
colours = ['tab:blue', 'tab:green', 'tab:purple']
labels = [r'Curve A', r'Curve B', r'Curve C', ]

y1_0 = [-2*np.pi, -2*np.pi, (4/3)*np.pi] # Values for the horizontal axis.
y2_0 = [2.3, 2.75, 0] # Values for the vertical axis.

sol = [] # Solution array.

t1 = 2

# Cycling through initial values for the angular velocity and amplitude.
for i in range(len(y1_0)):
    span = np.linspace(0, 200, 2000) # Defining a span for the data points that will be calculated.
    p0 = [y1_0[i], y2_0[i]] # Starting point of each solution curve.
    plt.plot(y1_0[i], y2_0[i], marker='o', markersize=4, color=colours[i], label=labels[i]) # Plotting 'p0'.
    sol.append(odeint(f, p0, span)) # Calculating solution array 'sol' for ODE 'f' starting on point 'p0' and with span 'span'.
    plt.plot(sol[i][:, 0], sol[i][:, 1], linestyle='-', linewidth=1, color=colours[i]) # Plotting the solution curve from the solution array 'sol'.
    
plt.legend(labelcolor='linecolor', fancybox=False, facecolor='white', edgecolor='black', framealpha=1) # Legend settings.