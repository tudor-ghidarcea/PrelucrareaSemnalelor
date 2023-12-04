#exercitiul 1. fereastra de tip hanning de dimensiunea 200
import scipy
from numpy.fft import fft, fftshift
import numpy as np
import matplotlib.pyplot as plt
def sine (amplitude, frequency, time, phase):
    return amplitude * np.sin (2 * np.pi * frequency * time + phase)

frequency = 100
amplitude = 10000
phase = 0

t = np.linspace(0, 9, 10, endpoint=False)

semnal = sine(amplitude, frequency, t, phase)

window = np.hanning(200)
plt.figure()

A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(mag)
response = np.clip(response, -100, 100)

plt.plot(freq, response)
plt.title("Frequency response of Hanning window")
plt.ylabel("Magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
plt.axis("tight")
plt.show()