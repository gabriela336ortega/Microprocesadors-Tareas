<<<<<<< HEAD
# Onda triangular

### Se reaiza una onda triangular en el siguiente codigo, cuya ascendencia es rapida y deciende lentamente. Se han importado desde machine a Pin y PWM, se ha determinado el Pin de salida (15), la frecuencia base de la onda y se ha delimitado a ser una onda de ascendencia rapida y descenso lento.

```python
from machine import Pin, PWM
import utime

pwm = PWM(Pin(15))
pwm.freq(5000)  # Frecuencia base

while True:
    for duty in range(0, 65535, 1000):  # Subida
        pwm.duty_u16(duty)
        utime.sleep(0.01)
    for duty in range(65535, 0, -1000):  # Bajada
        pwm.duty_u16(duty)
        utime.sleep(0.01)
=======
# Onda triangular

### Se reaiza una onda triangular en el siguiente codigo, cuya ascendencia es rapida y deciende lentamente. Se han importado desde machine a Pin y PWM, se ha determinado el Pin de salida (15), la frecuencia base de la onda y se ha delimitado a ser una onda de ascendencia rapida y descenso lento.

```python
from machine import Pin, PWM
import utime

pwm = PWM(Pin(15))
pwm.freq(5000)  # Frecuencia base

while True:
    for duty in range(0, 65535, 1000):  # Subida
        pwm.duty_u16(duty)
        utime.sleep(0.01)
    for duty in range(65535, 0, -1000):  # Bajada
        pwm.duty_u16(duty)
        utime.sleep(0.01)
>>>>>>> 71729b79ed4af81a01dce685868e93a49a66951c
```