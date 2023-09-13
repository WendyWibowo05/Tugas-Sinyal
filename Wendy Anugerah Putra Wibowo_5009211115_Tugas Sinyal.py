# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:35:10 2023

@author: Wendy Wibowo
"""

import numpy as np
import matplotlib.pyplot as plt

# Time Vektor
t = np.linspace(0, 1, 1000, endpoint=False)

# Noisy signal
signal = 0.5 * np.sin(2 * np.pi * 5 * t) + 0.3 * np.sin(2 * np.pi * 10 * t)
noise = 0.2 * np.random.normal(size=len(t))
noisy_signal = signal + noise

# Low Pass filter kernel
filter_kernel = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # Simple moving average filter

# konvolusi untuk memfilter signal noisy
filtered_signal = np.convolve(noisy_signal, filter_kernel, mode='same')

# Plot
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title("Original Signal")
plt.plot(t, noisy_signal, label='Noisy Signal')
plt.plot(t, signal, label='True Signal', linestyle='--')
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Filtered Signal (Low-pass)")
plt.plot(t, filtered_signal, color='green', label='Filtered Signal')
plt.legend()

plt.tight_layout()
plt.show()

# ID
print("Nama: Wendy Anugerah Putra Wibowo")
print("NRP: 5009211115")