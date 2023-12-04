import numpy as np
import matplotlib.pyplot as plt
import math

#exercitiul 1

def sine_wave_function(frequency, time):
    return 2 * np.sin(2 * np.pi * frequency * time + 3)

def transformed_function(frequency, time, omega):
    return sine_wave_function(time, frequency) * math.e**(-2 * np.pi * 1j * time * omega)

# Plecam de la o frecventa de 12
time_values = np.linspace(0, 12, 1600)
plt.plot(time_values, sine_wave_function(4, time_values))
plt.show()

# Omega = 1
without_omega = transformed_function(12, time_values, 1)
plt.plot(without_omega.real, without_omega.imag)
plt.show()

# Omega = 4
first_omega = transformed_function(12, time_values, 4)
plt.plot(first_omega.real, first_omega.imag)
plt.show()

# Omega = 5
second_omega = transformed_function(12, time_values, 5)
plt.plot(second_omega.real, second_omega.imag)
plt.show()

# Omega = 9
third_omega = transformed_function(12, time_values, 9)
plt.plot(third_omega.real, third_omega.imag)
plt.show()

# Omega = 15
fourth_omega = transformed_function(12, time_values, 15)
plt.plot(fourth_omega.real, fourth_omega.imag)
plt.show()

# exercitiul 2

def oscillation(amplitude, frequency,time):
    return amplitude * np.sin(2 * np.pi * frequency * time + 3)

time_points = np.linspace(0,4,1600)

def complex_wave(amplitude,frequency,time,omega):
    return oscillation(amplitude,time,frequency) * math.e**(-2*np.pi*1j*time*omega)

signal = oscillation(7,5,time_points) + oscillation(4,8,time_points) + oscillation(21,10,time_points)
plt.plot(time_points,signal)
plt.show()

transformed_signal = 0
for i in range(0,1600):
    transformed_signal += signal * math.e**((-2*np.pi*1j*i*time_points)/1600)

frequency_points = np.linspace(0,100,1600)
plt.plot(frequency_points,abs(transformed_signal))
plt.show()
