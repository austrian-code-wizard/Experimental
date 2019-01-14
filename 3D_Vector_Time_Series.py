import numpy as np
import sys
import os
import csv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from mpl_toolkits.mplot3d import Axes3D
from math import cos, sin
from datetime import datetime
from time import sleep

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

def cross_product(v1, v2):
	zx = v1[1]*v2[2]-v1[2]*v2[1]
	zy = v1[2]*v2[0]-v1[0]*v2[2]
	zz = v1[0]*v2[1]-v1[1]*v2[0]
	return [zx, zy, zz]


origin = [0,0,0]
X, Y, Z = zip(origin,origin,origin)

if not os.path.exists(sys.argv[1]):
	exit(1)
input_file = open(sys.argv[1])
reader = csv.reader(input_file)
row = next(reader)
arrays_x = []
arrays_y = []
times = []
start_time = None
try:
	row = next(reader)
	start_time = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
	while True:
		Ux, Vx, Wx = zip(euler_x(float(row[1]), float(row[2]), float(row[3])))
		Uy, Vy, Wy = zip(euler_y(float(row[1]), float(row[2]), float(row[3])))
		new_array_x = [X, Y, Z, Ux, Vx, Wx]
		new_array_y = [X, Y, Z, Uy, Vy, Wy]
		arrays_x.append(new_array_x)
		arrays_y.append(new_array_y)
		times.append((datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")-start_time).total_seconds())
		row = next(reader)

except Exception as e:
	print(e)
	pass

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X,Y,Z, 0.06, 0, 0 ,arrow_length_ratio=0.01, color='red')
ax.quiver(X,Y,Z, 0, 0.06, 0 ,arrow_length_ratio=0.01, color='blue')
ax.quiver(X,Y,Z, 0, 0, 0.06, arrow_length_ratio=0.01, color='green')

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 1, len(arrays_x)-1, valinit=0, valstep=1)


def update(val):
	data_point = int(sfreq.val)
	ax.cla()
	ax.quiver(arrays_x[data_point][0], arrays_x[data_point][1],arrays_x[data_point][2],arrays_x[data_point][3],
			arrays_x[data_point][4],arrays_x[data_point][5], length=0.06, color='red')
	ax.quiver(arrays_y[data_point][0], arrays_y[data_point][1], arrays_y[data_point][2], arrays_y[data_point][3],
			arrays_y[data_point][4], arrays_y[data_point][5], length=0.06, color='blue')
	x_vector = [arrays_x[data_point][3][0], arrays_x[data_point][4][0], arrays_x[data_point][5][0]]
	print(x_vector)
	y_vector = [arrays_y[data_point][3][0], arrays_y[data_point][4][0], arrays_y[data_point][5][0]]
	print(y_vector)
	Uz, Vz, Wz = zip(cross_product(x_vector, y_vector))
	ax.quiver(X, Y, Z, Uz, Vz, Wz, length=0.06, color='green')
	fig.canvas.set_window_title("Seconds after start: " + str(times[data_point]))
	fig.canvas.draw_idle()
sfreq.on_changed(update)

def show_animation():
	last_one = 0
	for i in range(0, len(arrays_x)):
		update(i)
		sleep(times[i]-last_one)
		last_one = times[i]

	pass

plt.show()
