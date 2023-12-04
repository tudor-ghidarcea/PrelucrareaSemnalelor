#laboratorul 4
# exercitiul 1a
#un esantion la doa ore = 1 esantion la 7200 de secunde = frecventa de 0.000138 Hz
# exercitiul 1b
# un ciclu dureaza 24 de ore ( de la 1 grad la - 1 grad si inapoi la un grad), deci atata este perioada semnalului
#de temperatura
# frecventa semnaluui de temperatura este inversul duratei sale, deci 1/24 de ore, deci
# 1/50,400 deci 0.0000198 Hz
# intervalul de timp minim la care trebuie masurata temperatura pentru a satisface principiul Nyquist
# este dublul frecventei, deci 0.0000396
#exercitiul 1c
import scipy
import numpy as np
import matplotlib.pyplot as plt
fig, axs = plt.subplots(3)
t = np.linspace(0, 1, 10, endpoint=False)
x = np.sin(2 * np.pi * 100 * t)
axs[0].plot(t,x)
axs[0].stem(t, x)

#exercitiul 2
x = np.linspace(3,7,100)

y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x,y, 'b-')
plt.show()

#exercitiu 3

# (2fc-b) /m >= fs >= (2fc + b) /m+1
# fs > 2b
# b = 10 hz
# fc = 90hz
# m = 1,2,4
# pentru m = 1:
# (180hz-10hz)/1 >= fs >= (180Hz+10Hz)/2
#
# 170hz >= fs >= 95hz
# fs = (95Hz, 170 Hz)
#
# pentru m = 2:
#
# (180Hz-10Hz)/2 >= fs >= (180hz+10Hz)3
#
# 85Hz >= fs >= 63.33Hz
#
# fs = (63.3Hz, 85Hz)
#
# pentru m = 4:
#
# (180Hz-10Hz)/4 >= fs >= (180Hz+10Hz)/5
#
# 42.5Hz >= fs >= 38Hz
#
# fs = (38Hz, 42.5Hz)