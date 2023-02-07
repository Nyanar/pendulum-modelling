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
plt.xlim([0, 20])
plt.ylim([-1.3, 1.3])
#plt.xticks(np.arange(-2*np.pi, 2*np.pi+np.pi, step=(np.pi)), [r'$-2\pi$',r'$-\pi$',r'0',r'$\pi$',r'$2\pi$'])
plt.yticks(np.arange(-1, 1+1, step=(1)), [r'$-\theta_0$', r'$0$', r'$\theta_0$'])
plt.grid(which='major', axis='both', color='gray', linestyle='-', linewidth=0.1)

b = 0.3 # Friction coefficient.
t = 0 # Time.
m = 1 # Mass.
g = 10 # Gravitational acceleration.
L = 10 # Length.

c_1=1
c_2=0

zin = np.linspace(0, 20, 300)

z_0 = 1

def f(t):
    return np.e**(-(b*t/(2*m)))*(c_1*np.cos(t*np.sqrt(abs((b/m)**2-4*(g/L))/2))+c_2*np.sin(t*np.sqrt(abs((b/m)**2-4*(g/L))/2)))

plt.plot(zin, f(zin), color='tab:green')

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='square', facecolor='white', alpha=1)

# place a text box in upper left in axes coords
plt.text(16, 1.1, r'$\!\!\!\!\ell\ =10\\[6pt]b\ =0.4\\[6pt]\dot{\theta_0}=0$', fontsize=22,
        verticalalignment='top', bbox=props)

#plt.savefig('/home/pedro/Desktop/IA\'/damped1.png', dpi=400, facecolor='w', edgecolor='w') # Saving figure.