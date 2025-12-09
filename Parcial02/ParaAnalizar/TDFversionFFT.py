import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# TIPO DE SEÑAL: "seno", "cuadrada", "triangular".

tipo = "triangular" 

# VALORES DE MUESTREO GENERALES

fs = 10000                                           # frecuencia de muestreo
N = 10                                            # número de muestras
t = np.linspace(0, N/fs, N, endpoint=False)

# Cálculo de la señal según el tipo.

if tipo == "seno":
    f0 = 50      # frecuencia
    A = 2        # Amplitud
    x = A * np.sin(2*np.pi*f0*t)

elif tipo == "cuadrada":
    f0 = 20      # Frecuencia
    A = 3        # Amplitud
    x = A * signal.square(2*np.pi*f0*t)

elif tipo == "triangular":
    f0 = 5000      # Frecuencia en Hz
    A = 3.3      # Amplitud de ejemplo
    x = A * signal.sawtooth(2*np.pi*f0*t, 0.5) # 0.5 determina la forma perfecta triangular

else:
    raise ValueError("Tipo de señal no válido. Usa: seno, cuadrada o triangular.")

# FFT 
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, d=1/fs)
magnitudes = np.abs(X)/N

# Gráficas
plt.subplot(2,1,1)
plt.plot(t, x)
plt.title(f"Señal en el tiempo ({tipo})")

plt.subplot(2,1,2)
plt.plot(freqs[:N//2], magnitudes[:N//2])
plt.title("Espectro FFT")
plt.show()