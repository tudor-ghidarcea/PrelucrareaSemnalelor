import scipy
import numpy as np
import matplotlib.pyplot as plt
#laboratorul 3
#exercitiu 1
#frecventa de 100 herzi, esantionata sub nyquist, la 100hz
fig, axs = plt.subplots(3)
t = np.linspace(0, 1, 10, endpoint=False)
x = np.sin(2 * np.pi * 100 * t)
axs[0].plot(t,x)
axs[0].stem(t, x)



#frecventa de 200 herzi, esantionata tot la 100hz
x = np.sin(2 * np.pi * 200 * t)
axs[1].plot(t,x)
axs[1].stem(t, x)


#frecventa de 400hz, esantionata tot la 100hz
x = np.sin(2 * np.pi * 400 * t)
axs[2].plot(t,x)
axs[2].stem(t, x)
plt.show()

#exercitiul 2
#luam aceleasi trei semnale, esantionate deasupra frecventei ntquist, deci luam 900hz deoarece
#este deasupra frecventelor nyquist aferente fiecarui semnal. O frecventa mai mare de esantionare
#inseamna ca putem reproduce mai usor semnalul original, nu poate produce aliere
fig, axs = plt.subplots(3)
t = np.linspace(0, 9, 10, endpoint=False)
x = np.sin(2 * np.pi * 100 * t)
axs[0].plot(t,x)
axs[0].stem(t, x)


t = np.linspace(0, 9, 10, endpoint=False)
x = np.sin(2 * np.pi * 200 * t)
axs[1].plot(t,x)
axs[1].stem(t, x)


t = np.linspace(0, 9, 10, endpoint=False)
x = np.sin(2 * np.pi * 400 * t)
axs[2].plot(t,x)
axs[2].stem(t, x)
plt.show()

# exercitiul 3
# daca instrumentul produce sunete intre frecventele de 40 si 200hz,
# frecventa de lowpass necesara pentru a reprezenta corect semnalul
# in urma esantionarii este de 400hz

#exercitiul 6
# Puterea unui semnal este Psemnal = 90dB.
# Se cunoas, te raportul semnalzgomot, SNRdB = 80dB.
# Care este puterea zgomotului?
#snr=80
#Ps=90
#SNR= Ps/Pz = 90/Pz=80
#90/Pz=80=> puterea zgomotului este de 1.125

