import matplotlib.pyplot as plt
import numpy as np

# Ch4.00 - Intro 
# x = np.linspace(0, 10, 100)
# 
# fig, ax = plt.subplots(2)
# 
# ax[0].plot(x, np.sin(x), '-')
# ax[1].plot(x, np.cos(x), '--')

# Ch4.01 - Simple Line Plots
fig1 = plt.figure()
ax1 = plt.axes()

x = np.linspace(0, 10, 1000)

ax1.plot(x, np.sin(x-0), color='blue') # Specify color by name
ax1.plot(x, np.sin(x-1), color='g') # short color code (rgbcmyk)
ax1.plot(x, np.sin(x-2), color='0.75') # Gray Scale
ax1.plot(x, np.sin(x-3), color='#FFDD44') # Hex code (RRGGBB from 00 to FF)
ax1.plot(x, np.sin(x-4), color=(1.0, 0.2, 0.3)) # RGB tuple, values 0 to 1
ax1.plot(x, np.sin(x-5), color='chartreuse')

fig2 = plt.figure()
ax2 = plt.axes()

ax2.plot(x, x+0, linestyle='-') # solid
ax2.plot(x, x+1, linestyle='--') # dashed
ax2.plot(x, x+2, linestyle='-.') # dashdot
ax2.plot(x, x+3, linestyle=':') # dotted

fig3 = plt.figure()
ax3 = plt.axes()

ax3.plot(x, np.sin(x))
ax3.set_xlim(-1, 11)
ax3.set_ylim(-1.5, 1.5)

plt.show()
