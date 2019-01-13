import numpy as np
import sys
import os
import csv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D
from math import cos, sin

def euler_x(heading, roll, pitch):
	x = cos(heading)*cos(pitch)
	y = sin(heading)*cos(pitch)
	z = sin(pitch)
	return [x, y, z]

def euler_y(heading, roll, pitch):
	x = -cos(heading)*sin(pitch)*sin(roll) - sin(heading)*cos(roll)
	y = -sin(heading)*sin(pitch)*sin(roll) + cos(heading)*cos(roll)
	z = cos(pitch)*sin(roll)
	return [x, y, z]


origin = [0,0,0]
X, Y, Z = zip(origin,origin,origin)

if not os.path.exists(sys.argv[1]):
	exit(1)
input_file = open(sys.argv[1])
reader = csv.reader(input_file)
row = next(reader)
arrays_x = []
arrays_y = []
try:
	while True:
		row = next(reader)
		print(row)
		Ux, Vx, Wx = zip(euler_x(float(row[1]), float(row[2]), float(row[3])))
		Uy, Vy, Wy = zip(euler_y(float(row[1]), float(row[2]), float(row[3])))
		new_array_x = [X, Y, Z, Ux, Vx, Wx]
		new_array_y = [X, Y, Z, Uy, Vy, Wy]
		arrays_x.append(new_array_x)
		arrays_y.append(new_array_y)
except Exception as e:
	print(e)
	pass

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X,Y,Z, 0.1, 0, 0 ,arrow_length_ratio=0.01)
ax.quiver(X,Y,Z, 0, 0.1, 0 ,arrow_length_ratio=0.01)

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 1, len(arrays_x)-1, valinit=0, valstep=1)


def update(val):
	global arrays

	data_point = int(sfreq.val)
	ax.cla()
	ax.quiver(arrays_x[data_point][0], arrays_x[data_point][1],arrays_x[data_point][2],arrays_x[data_point][3],
			  arrays_x[data_point][4],arrays_x[data_point][5], length=0.01)
	ax.quiver(arrays_y[data_point][0], arrays_y[data_point][1], arrays_y[data_point][2], arrays_y[data_point][3],
			  arrays_y[data_point][4], arrays_y[data_point][5], length=0.01)
	fig.canvas.draw_idle()
sfreq.on_changed(update)

plt.show()
