import numpy as np
import matplotlib.pyplot as plt

def analizar_fft(x, fs):
    N = len(x)
    X = np.fft.fft(x)
    magnitudes = np.abs(X) / N
    freqs = np.fft.fftfreq(N, d=1/fs)

    idx = np.where(freqs >= 0)
    freqs_pos = freqs[idx]
    magnitudes_pos = magnitudes[idx]

    plt.figure(figsize=(10,5))
    plt.plot(freqs_pos, magnitudes_pos)
    plt.title("Espectro FFT de la señal")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.show()

    return freqs_pos, magnitudes_pos

# Tus valores
fs = 1000                         # frecuencia de muestreo
t = np.linspace(0, 1, 1000)       # vector de tiempo dado por (t = np.linspace(0, N/fs, N)
x = 2 * np.abs((t % 0.1) - 0.05)  # onda triangular simulada

analizar_fft(x, fs)