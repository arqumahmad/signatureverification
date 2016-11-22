import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook




#getting data from csv file
data = np.genfromtxt('2.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])
fig = plt.figure()

#data
s=data['s'] #sample nos
p=data['p'] # pressure
x=data['x'] #x-coordinate
y=data['y'] #y-coordinate

#calculating dy/dx
dx = np.diff(data['x'])
dy = np.diff(data['y'])
a = np.arctan2(dy,dx) * 180 / np.pi
l= np.arange(1,len(dx)+1)

dist=np.sqrt((dx**2)+dy**2)
vel = dist/l
acc=vel/l









#ax1 = fig.add_subplot(411)


#plotting graph
ax1 = fig.add_subplot(321)
ax1.set_title("Pressure")
ax1.plot(s, p, color='b', marker='o')


ax4 = fig.add_subplot(322)
ax4.set_title("Angle")
ax4.plot(l, a, color='g')

ax2 = fig.add_subplot(323)
ax2.set_title("X")
ax2.plot(s, x, color='c')

ax3 = fig.add_subplot(324)
ax3.set_title("Y")
ax3.plot(s, y, color='m')


ax4 = fig.add_subplot(325)
ax4.set_title("Velocity")
ax4.plot(l, vel, color='y', marker='o')

ax4 = fig.add_subplot(326)
ax4.set_title("Acceleration")
ax4.plot(l, acc, color='k', marker='o')
plt.tight_layout()
fig = plt.gcf()

plt.show()
