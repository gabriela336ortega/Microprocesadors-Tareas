# La FFT o Transformada Rápida de Fourier.

## Es un algoritmo que calcula la Transformada discreta de Fourier (TDF) de una señal, pero de manera mucho más eficiente. La TDF convierte una señal del dominio del tiempo al dominio de la frecuencia. El presente código realizado con lenguaje de programación pyhton convierte la FFT en una función que devuelve *valores*, *magnitudes*, *fases* y *frecuencia*. Se ha refactorizado el código para imprimir los resultados en orden y entendibles uniendo la FFT, IDTF y DTF.

### archivo fourier.py. Aqui unicamente está el código de la FFT
```python
import math
import cmath

from fourier.core.fourier_response import FFTResponse
class Fourier:
    def __init__(self) -> None:
        pass

    def fft(self, x: list[complex]) -> list[complex]:
        """
        Implementación recursiva de la FFT (Cooley–Tukey).
        Se llama a sí misma.

        Args:
            x : List[complex]  -> lista de muestras reales o complejas

        Return:
            List[complex]      -> coeficientes complejos de la FFT
        """
        N: int = len(x)

        # Caso base
        if N <= 1:
            return x

        # FFT recursiva en índices pares e impares
        X_even: list[complex] = self.fft(x[0::2])
        X_odd:  list[complex] = self.fft(x[1::2])

        # Factores twiddle
        T: list[complex] = [
            cmath.exp(-2j * math.pi * k / N) * X_odd[k]
            for k in range(N // 2)
        ]

        # Combinar resultados (butterfly)
        return (
            [X_even[k] + T[k] for k in range(N // 2)] +
            [X_even[k] - T[k] for k in range(N // 2)]
        )

    def mi_fft(self, x: list[float], fs: float = 1.0) -> FFTResponse:
        """
        Calcula FFT sin NumPy y devuelve todo tipado.

        Args:
            x  : List[float]  -> señal de entrada
            fs : float        -> frecuencia de muestreo

        Return:
            FFTResponse: respuesta formateada de componentes de fourier
        """

        N: int = len(x)

        # Convertir a complejos
        x_complex: list[complex] = [complex(v) for v in x]

        # 1. FFT
        valores_fft: list[complex] = self.fft(x_complex)

        # 2. Magnitudes
        magnitudes: list[float] = [abs(v) for v in valores_fft]

        # 3. Fases
        fases: list[float] = [cmath.phase(v) for v in valores_fft]

        # 4. Vector de frecuencias
        freqs: list[float] = []
        for k in range(N):
            if k < N // 2:
                freqs.append(k * fs / N)
            else:
                freqs.append((k - N) * fs / N)
        
        result = FFTResponse(
            valores=valores_fft,
            magnitudes=magnitudes,
            fases=fases,
            frecuencias=freqs
        )

        return result
```
# TDF y TDIF.

### De maria.py

```python
import logging
import cmath
import math
from typing import List

class TransformadaDFT:
   
    def __init__(self):
        self.logger = logging.getLogger(f'[{self.__class__.__name__}]')
        self.logger.info("Inicializando analizador de Fourier...")

    def dft(self, x: List[float]) -> List[complex]:
        """
        Ejecuta una transformada discret de Fourier

        Args:
            x(List): Numeros reales de la muestra de la senal
        
        Returns:
            List[complex]: Lista de numeros complejos
        """
        self.logger.info("Iniciando transformada de fourier")
        N = len(x)
        X = []
        self.logger.info(f"Analizando {N} muestras")
        for k in range(N):
            suma = 0
            for n in range(N):
                angulo = -2j * math.pi * n * k / N
                suma += x[n] * cmath.exp(angulo)
            X.append(suma)
        return X

    def idft(self, X):
        N = len(X)
        x_rec = []
        for n in range(N):
            suma = 0
            for k in range(N):
                angulo = 2j * math.pi * n * k / N
                suma += X[k] * cmath.exp(angulo)
            x_rec.append(suma / N)
        return x_rec

```

## El archivo main.py importa todas las clases realizadas y las librerías para optimizar el código y mejorarlo visualmente.

### De main.py

```python
import math
import logging
from fourier.core import TransformadaDFT
from fourier.core import Fourier

if __name__ == "__main__":
    transformada = Fourier()

    fs = 100  # frecuencia de muestreo
    N = 32    # muestras

    t = [n / fs for n in range(N)]
    x = [2 * math.sin(2 * math.pi * 5 * ti) for ti in t]

    resultado = transformada.mi_fft(x, fs)

    valores = resultado.valores
    i = 0
    for valor in valores:
        print(f"Resultado {i} es: {valor}")
        i = i + 1


    logging.basicConfig(level="INFO")

    t = TransformadaDFT()
    x = [1, 2, 3, 4]

    print("DFT:", t.dft(x))
    #print("IDFT:", t.idft(t.dft(x)))
```

