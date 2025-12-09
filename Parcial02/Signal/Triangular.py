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
