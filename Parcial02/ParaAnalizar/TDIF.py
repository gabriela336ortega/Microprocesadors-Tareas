import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Tipo de señal: "seno", "cuadrada", "triangular"
tipo = "triangular"

# VALORES DE MUESTREO GENERALES
fs = 10000                                   # Frecuencia de muestreo
N = 100                                      # Número de muestras
t = np.linspace(0, N/fs, N, endpoint=False)

# Cálculo de la señal según el tipo

if tipo == "seno":
    f0 = 50
    A = 2
    x = A * np.sin(2*np.pi*f0*t)

elif tipo == "cuadrada":
    f0 = 20
    A = 3
    x = A * signal.square(2*np.pi*f0*t)

elif tipo == "triangular":
    f0 = 1000
    A = 3.3
    x = A * signal.sawtooth(2*np.pi*f0*t, 0.5)

else:
    raise ValueError("Tipo de señal no válido. Usa: seno, cuadrada o triangular.")

# TDF 
X = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

# TDIF
x_rec = np.zeros(N, dtype=complex)
for n in range(N):
    for k in range(N):
        x_rec[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
    x_rec[n] /= N   # normalización

# Magnitudes espectrales
magnitudes = np.abs(X) / N
freqs = np.arange(N) * fs / N

# Gráficas
plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.title(f"Señal original en el tiempo ({tipo})")

plt.subplot(3,1,2)
plt.plot(freqs[:N//2], magnitudes[:N//2])
plt.title("Espectro TDF (implementación directa)")

plt.subplot(3,1,3)
plt.plot(t, np.real(x_rec))
plt.title("Señal reconstruida con TDIF")
plt.tight_layout()
plt.show()