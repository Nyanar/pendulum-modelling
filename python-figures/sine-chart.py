# Importing mathematics packages.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 22})
rc('text', usetex=True)
plt.rcParams['grid.linewidth'] = 0.1

# Plot settings.
figure = plt.figure(figsize=(8, 5.5), dpi=400)
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta$')
plt.xlim([0, 2*np.pi])
plt.ylim([-1.3, 1.3])
#plt.xticks(np.arange(-2*np.pi, 2*np.pi+np.pi, step=(np.pi)), [r'$-2\pi$',r'$-\pi$',r'0',r'$\pi$',r'$2\pi$'])
plt.yticks(np.arange(-1, 1+1, step=(1)), [r'$-\theta_0$', r'$0$', r'$\theta_0$'])
plt.grid(which='major', axis='both', color='gray', linestyle='-', linewidth=0.1)

q = 0.2 # Friction coefficient.
t = 0 # Time.
m = 1 # Mass.
g = 10 # Gravitational acceleration.
L = 10 # Length.

zin = np.linspace(0, 20, 300)

z_0 = 1

def f(t):
    return z_0*np.cos(g/L*t)

plt.plot(zin, f(zin), color='tab:green')

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='square', facecolor='white', alpha=1)

# place a text box in upper left in axes coords
plt.text(2.7, 0.95, r'$\ell=10$', fontsize=22,
        verticalalignment='top', bbox=props)

plt.savefig('/home/pedro/Desktop/IA\'/shm1.png', dpi=400, facecolor='w', edgecolor='w') # Saving figure.