import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Tipo de señal: "seno", "cuadrada", "triangular"
tipo = "triangular"

# VALORES DE MUESTREO GENERALES
fs = 10000                                     # frecuencia de muestreo
N = 100                                        # número de muestras
t = np.linspace(0, N/fs, N, endpoint=False)

# Calculo segun el tipo de signal.

if tipo == "seno":
    f0 = 50
    A = 2
    x = A * np.sin(2*np.pi*f0*t)

elif tipo == "cuadrada":
    f0 = 20
    A = 3
    x = A * signal.square(2*np.pi*f0*t)

elif tipo == "triangular":
    f0 = 5000
    A = 3.3
    x = A * signal.sawtooth(2*np.pi*f0*t, 0.5)

else:
    raise ValueError("Tipo de señal no válido. Usa: seno, cuadrada o triangular.")

# TDF
X = np.zeros(N, dtype=complex)   # vector para la transformada
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

magnitudes = np.abs(X) / N
freqs = np.arange(N) * fs / N

# Gráficas
plt.subplot(2,1,1)
plt.plot(t, x)
plt.title(f"Señal en el tiempo ({tipo})")

plt.subplot(2,1,2)
plt.plot(freqs[:N//2], magnitudes[:N//2])
plt.title("Espectro TDF (implementación directa)")
plt.show()