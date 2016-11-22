import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook




#getting data from csv file
data1 = np.genfromtxt('database/30/4.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])
data2 = np.genfromtxt('database/30/5.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])
data3 = np.genfromtxt('database/35/18.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])
data4 = np.genfromtxt('database/35/18.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])
data5 = np.genfromtxt('database/30/20.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])
data6 = np.genfromtxt('database/32/19.csv', delimiter=',', names=['s', 'x', 'y', 'p' ])

fig = plt.figure()

#data
s1=data1['s'] #sample nos
p1=data1['p'] # pressure
x1=data1['x'] #x-coordinate
y1=data1['y'] #y-coordinate

s2=data2['s'] #sample nos
p2=data2['p'] # pressure
x2=data2['x'] #x-coordinate
y2=data2['y'] #y-coordinate

s3=data3['s'] #sample nos
p3=data3['p'] # pressure
x3=data3['x'] #x-coordinate
y3=data3['y'] #y-coordinate

s4=data4['s'] #sample nos
p4=data4['p'] # pressure
x4=data4['x'] #x-coordinate
y4=data4['y'] #y-coordinate

s5=data5['s'] #sample nos
p5=data5['p'] # pressure
x5=data5['x'] #x-coordinate
y5=data5['y'] #y-coordinate

s6=data6['s'] #sample nos
p6=data6['p'] # pressure
x6=data6['x'] #x-coordinate
y6=data6['y'] #y-coordinate

#calculating dy/dx
#dx = np.diff(data['x'])
#dy = np.diff(data['y'])
#a = np.arctan2(dy,dx) * 180 / np.pi
#l= np.arange(1,len(dx)+1)

#dist=np.sqrt((dx**2)+dy**2)
#vel = dist/l
#acc=vel/l









#ax1 = fig.add_subplot(411)


#plotting graph
ax11 = fig.add_subplot(631)
ax11.set_title("Pressure")
ax11.plot(s1, p1, color='b', marker='o')

ax12 = fig.add_subplot(632)
ax12.set_title("X")
ax12.plot(s1, x1, color='c')

ax13 = fig.add_subplot(633)
ax13.set_title("Y")
ax13.plot(s1, y1, color='m')

ax21 = fig.add_subplot(634)
ax21.set_title("Pressure")
ax21.plot(s2, p2, color='b', marker='o')

ax22 = fig.add_subplot(635)
ax22.set_title("X")
ax22.plot(s2, x2, color='c')

ax23 = fig.add_subplot(636)
ax23.set_title("Y")
ax23.plot(s2, y2, color='m')

ax31 = fig.add_subplot(637)
ax31.set_title("Pressure")
ax31.plot(s5, p5, color='b', marker='o')

ax32 = fig.add_subplot(638)
ax32.set_title("X")
ax32.plot(s5, x5, color='c')

ax33 = fig.add_subplot(639)
ax33.set_title("Y")
ax33.plot(s5, y5, color='m')







#plt.tight_layout()
fig = plt.gcf()

plt.show()
