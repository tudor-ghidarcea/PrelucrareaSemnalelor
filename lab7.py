#exercitiul 1
# a)Amplitudinea semnalului din figura 1 este 2.
# b)In figura 1 valoarea 2 apare in fiecare punct maxim si minim al graficului(3 si 7).
# c)Componenta continua a semnalului din figura 1 este 5.
# d)Formula pentru semnalul reprezentat din figura 1 este 5+2*cos(2*pi*40*t)

# a)Frecventa de esantionare este 1/7200=0.000138888889.
# b)Esantioanele din fisier acopera o perioada de 762 zile.
# c)Frecventa maxima prezenta in semnal este 1/3600=0.000277777778.

import numpy as np
import numpy as np
import matplotlib.pyplot as plt
x = np.genfromtxt("trafic.csv", delimiter=" ")
X = np.fft.fft(x)
print(len(x))
N=18288
x = abs(x/N)
x = x[:9144]
f = 1/3600*np.linspace(0,9144,9144)/N

samplingFrequency = 100

samplingInterval = 1 / samplingFrequency

beginTime = 0

endTime = 10

signal1Frequency = 4

signal2Frequency = 7

time = np.arange(1, len(x), 1)

amplitude = np.sin(2 * np.pi * 1/7200 * time)

fourierTransform = np.fft.fft(amplitude) / len(amplitude)

fourierTransform = fourierTransform[range(int(len(amplitude) / 2))]

tpCount = len(amplitude)

values = np.arange(int(tpCount / 2))

timePeriod = tpCount / samplingFrequency

frequencies = values / timePeriod

plt.plot(frequencies, abs(fourierTransform))

plt.show()