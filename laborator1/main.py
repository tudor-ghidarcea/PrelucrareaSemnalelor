import numpy as np
import matplotlib.pyplot as plt
#Ghidarcea Tudor Alexandru, 341, laborator1
#1
#a)

def cos(amplitude, frequency, phase, time):
    return amplitude * np.cos(2 ** np.pi * frequency * time + phase)

#b)
#x(t)
amplitude = 1
frequency = 260
phase = np.pi / 3
time_of_view = 0.03 #%s
n_samples = int(10e5)
atime_x = np.linspace(0, time_of_view, n_samples)
asignal_x = cos(amplitude, frequency, phase, atime_x)

plt.plot(atime_x, asignal_x)
plt.grid("grid")
plt.show()
#y(t)

amplitude = -1
frequency = 140
phase = -np.pi / 3
time_of_view = 0.03 #%s
n_samples = int(10e5)
atime_y = np.linspace(0, time_of_view, n_samples)
asignal_y = cos(amplitude, frequency, phase, atime_x)
plt.plot(atime_y, asignal_y)
plt.grid("grid")
plt.show()

#z(t)

amplitude = 1
frequency = 60
phase = np.pi / 3
time_of_view = 0.03 #%s
n_samples = int(10e5)
atime_z = np.linspace(0, time_of_view, n_samples)
asignal_z = cos(amplitude, frequency, phase, atime_z)
plt.plot(atime_z, asignal_z)
plt.grid("grid")
plt.show()
#c) x(n)
amplitude = 1
frequency = 260
phase = np.pi / 3
time_pf_view=0.03
atime = np.linspace(0, time_of_view, n_samples)
asignal = cos(amplitude, frequency, phase, atime)
n_samples = int(time_of_view/(1/200))
plt.stem(atime, asignal)
plt.grid("grid")
plt.show()

#y(n)
amplitude = 1
frequency = 140
phase = -p.pi / 3
time_pf_view=0.03
atime = np.linspace(0, time_of_view, n_samples)
asignal = cos(amplitude, frequency, phase, atime)
n_samples = int(time_of_view/(1/200))
plt.stem(atime, asignal)
plt.grid("grid")
plt.show()

#z(n)

amplitude = 1
frequency = 60
phase = p.pi / 3
time_pf_view=0.03
atime = np.linspace(0, time_of_view, n_samples)
asignal = cos(amplitude, frequency, phase, atime)
n_samples = int(time_of_view/(1/200))
plt.stem(atime, asignal)
plt.grid("grid")
plt.show()

