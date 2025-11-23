<<<<<<< HEAD
<<<<<<<< HEAD:informeOnda.md
# Demostracion de valores de la señal triangular

### Éste primer codigo demuestra las propiedades de una señal triangular, importando el PWM e introduciendo los valores caracteristicos de la señal y el voltaje que recibe del Raspberry Pi Pico. El codigo nos proporciona los valores de el voltaje pico (Vp), voltaje pico a pico (Vpp), voltaje rms (Vrms), periodo (T) de la señal y el voltaje promedio (Vavg)

```python
from machine import Pin, PWM
import time, math

# Configuración PWM
pwm = PWM(Pin(15))
pwm.freq(5000)   # Frecuencia fija de 5 kHz
Vcc = 3.3        # Voltaje de salida del Pico

while True:
    for duty in range(0, 65535, 5000):  # Subida
        pwm.duty_u16(duty)
        duty_ratio = duty / 65535  # Duty normalizado (0 a 1)

        # Cálculos eléctricos
        Vp = Vcc
        Vpp = Vcc
        Vavg = duty_ratio * Vcc
        Vrms = math.sqrt(duty_ratio) * Vcc
        f = 5000
        T = 1 / f

        print(f"Duty={duty_ratio:.2f} | Vp={Vp:.2f} V | Vpp={Vpp:.2f} V | Vavg={Vavg:.2f} V | Vrms={Vrms:.2f} V | f={f} Hz | T={T*1e6:.1f} us")
        time.sleep(0.1)

    for duty in range(65535, 0, -5000):  # Bajada
        pwm.duty_u16(duty)
        duty_ratio = duty / 65535

        Vp = Vcc
        Vpp = Vcc
        Vavg = duty_ratio * Vcc
        Vrms = math.sqrt(duty_ratio) * Vcc
        f = 5000
        T = 1 / f

        print(f"Duty={duty_ratio:.2f} | Vp={Vp:.2f} V | Vpp={Vpp:.2f} V | Vavg={Vavg:.2f} V | Vrms={Vrms:.2f} V | f={f} Hz | T={T*1e6:.1f} us")
        time.sleep(0.1)
```
 # Valores Señal Triangular

 *f    = 5kHz*
 *Vpp  = 3.3V*
 *Vmed = 1.3V*
 *Vmin = 0V*
 *T = 200 us*
========
archivo Informe.md eliminado
>>>>>>>> 71729b79ed4af81a01dce685868e93a49a66951c:Informe.md
=======
# Demostracion de valores de la señal triangular

### Este primer codigo demuestra las propiedades de una señal triangular, importando el PWM e introduciendo los valores caracteristicos de la señal y el voltaje que recibe del Raspberry Pi Pico. El codigo nos proporciona los valores de el voltaje pico (Vp), voltaje pico a pico (Vpp), voltaje rms (Vrms), periodo (T) de la señal y el voltaje promedio (Vavg)

```python
from machine import Pin, PWM
import time, math

# Configuración PWM
pwm = PWM(Pin(15))
pwm.freq(5000)   # Frecuencia fija de 5 kHz
Vcc = 3.3        # Voltaje de salida del Pico

while True:
    for duty in range(0, 65535, 5000):  # Subida
        pwm.duty_u16(duty)
        duty_ratio = duty / 65535  # Duty normalizado (0 a 1)

        # Cálculos eléctricos
        Vp = Vcc
        Vpp = Vcc
        Vavg = duty_ratio * Vcc
        Vrms = math.sqrt(duty_ratio) * Vcc
        f = 5000
        T = 1 / f

        print(f"Duty={duty_ratio:.2f} | Vp={Vp:.2f} V | Vpp={Vpp:.2f} V | Vavg={Vavg:.2f} V | Vrms={Vrms:.2f} V | f={f} Hz | T={T*1e6:.1f} us")
        time.sleep(0.1)

    for duty in range(65535, 0, -5000):  # Bajada
        pwm.duty_u16(duty)
        duty_ratio = duty / 65535

        Vp = Vcc
        Vpp = Vcc
        Vavg = duty_ratio * Vcc
        Vrms = math.sqrt(duty_ratio) * Vcc
        f = 5000
        T = 1 / f

        print(f"Duty={duty_ratio:.2f} | Vp={Vp:.2f} V | Vpp={Vpp:.2f} V | Vavg={Vavg:.2f} V | Vrms={Vrms:.2f} V | f={f} Hz | T={T*1e6:.1f} us")
        time.sleep(0.1)
```
 # Valores Señal Triangular

 *f    = 5kHz*
 *Vpp  = 3.3V*
 *Vmed = 1.3V*
 *Vmin = 0V*
 *T = 200 us*
>>>>>>> 71729b79ed4af81a01dce685868e93a49a66951c
