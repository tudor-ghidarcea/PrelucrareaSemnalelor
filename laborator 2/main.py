#Laboratorul 1
# 2.  Generat,i urm ̆atoarele semnale s,i afis,at,i-le grafic, fiecare ˆıntr-un plot:
# (a)  Un semnal sinusoidal de frecvent, ̆a 400 Hz, care s ̆a cont,in ̆a 1600 dees,antioane.
# (b)  Un semnal sinusoidal de frecvent, ̆a 800 Hz, care s ̆a dureze 3 secunde.
# (c)  Un semnal de tipsawtoothde frecvent, ̆a 240 Hz
# (putet,i folosi funct,iilenumpy.floorsaunumpy.mod).
# (d)  Un semnal de tipsquarede frecvent, ̆a 300 Hz (putet,i folosi funct,ianumpy.sign).
# (e)  Un semnal 2D aleator. Creat,i unnumpy.arrayde dimensiune 128x128s,
# i init,ializat,i-l aleator, folosindnumpy.random.rand(x,y),
# unde x s,iy reprezint ̆a num ̆arul de linii respectiv de coloane.
# Afis,at,i semnalulgenerat folosind funct,iaimshow(I)dinmatplotlib.
# (f)  Un  semnal  2D  la  alegerea  voastr ̆a.
# Creat,i  unnumpy.arrayde  di-mensiune 128x128 s,i init,ializat,i-l folosind o procedur
# ̆a creat ̆a de voi.Utilizat,i, spre exemplu, funct,iilenumpy.zeros()s,inumpy.ones().
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#a
# 1/T = 400 => T = 0,0025 perioada de esantionare
# Timpul = 0,0025 * 1600 (nr de esantioane) = 4

time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.sin(2* np.pi * time_of_view_2a))
#plt.show()

#b
# 1/T = 800 => T = 0,000125 perioada de esantionare
# Timpul = 0,000125 * 24000 (nr de esantioane) = 3

time_of_view_2b = np.linspace(0, 3, 24000)
plt.plot(time_of_view_2b, np.sin(2* np.pi * time_of_view_2b))
#plt.show()


#c
# 1/T = 400 => T = 0,0025 perioada de esantionare
# Timpul = 0,0025 * 1600 (nr de esantioane) = 4
#sawtooth frecv. 240Hz
time_of_view_2c=np.linspace(0, 1, 500)
plt.plot(time_of_view_2c, signal.sawtooth(2 * np.pi * 240 * time_of_view_2c))
#plt.show()

#d

time_of_view_2d= np.linspace(0, 1, 100, endpoint = True)
plt.plot(time_of_view_2d, signal.square(2 * np.pi * 300 * time_of_view_2d))
#plt.show()

#e
array = [np.random.rand(128,128)]
array = np.reshape(array, (128, 128))
plt.step(np.arange(0, len(array)), array)
plt.imshow(array)
#plt.show()

#f
f = np.zeros([128,128], dtype=int)
f= np.reshape(f, (128, 128))
plt.step(np.arange(0, len(f)), f)
plt.imshow(f)
#plt.show()

#Laboratorul 2

#1
time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.cos(2* np.pi * time_of_view_2a))
#plt.show()

time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.sin(2* np.pi * time_of_view_2a+ np.pi/2))
#plt.show()

#2

time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.sin(2* np.pi * time_of_view_2a+np.pi/2))
#plt.show()

time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.sin(2* np.pi * time_of_view_2a+ np.pi/3))
#plt.show()

time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.sin(2* np.pi * time_of_view_2a+2*np.pi))
#plt.show()

time_of_view_2a = np.linspace(0, 4, 1600)
plt.plot(time_of_view_2a, np.sin(2* np.pi * time_of_view_2a+ np.pi+1))
#plt.show()

#3
#a
import sounddevice
fs=44100
sounddevice.play(np.sin(2* np.pi * time_of_view_2a+2*np.pi), fs)
#b
sounddevice.play(np.sin(2* np.pi * time_of_view_2b+2*np.pi), fs)
#c
sounddevice.play(np.sin(2* np.pi * time_of_view_2c+2*np.pi), fs)
#d
sounddevice.play(np.sin(2* np.pi * time_of_view_2d+2*np.pi), fs)


import scipy
from scipy import io
rate = int(10e5)
scipy.io.wavfile.write('nume.wav', rate, np.linspace(0, 4, 1600))

#4
time_of_view_5 = np.linspace(0, 4, 1600)
plt.plot(time_of_view_5, np.sin(2* np.pi * time_of_view_5))


time_of_view_5 = np.linspace(0, 4, 1600)
plt.plot(time_of_view_5, np.square( time_of_view_5))

plt.plot(time_of_view_5, np.sin(2* np.pi * time_of_view_5)+time_of_view_5, np.square( time_of_view_5))



#5
sounddevice.play(np.sin(2* np.pi * time_of_view_2d) + np.sin(2* np.pi * 100*time_of_view_2d), fs)
#frecventa mai inalta duce la sunet mai acut

#6
#1
fs = 10000
time_of_view=np.linspace(0,6,1000)
plt.plot(time_of_view, np.sin(2*np.pi)*(fs/2)*time_of_view)
#plt.show()
#2
plt.plot(time_of_view, np.sin(2*np.pi)*(fs/4)*time_of_view)
#plt.show()

#3
plt.plot(time_of_view, np.sin(2*np.pi)*0*time_of_view)
#plt.show()

#cu cat frecventa este mai mica, intervalul nu apuca sa se repete
# de la fel de multe ori intr-un interval de timp ales

#7
time_of_view_ = np.linspace(0, 4, 400)
plt.plot(time_of_view[2::4], np.sin(2*np.pi * 1000* time_of_view)[2::4])
plt.show()

#decimarea depinde de cum sunt luate punctele din 4 in 4, nu este invariata in timp