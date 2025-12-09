from machine import Pin, PWM
import time, math

# Configuración PWM
pwm = PWM(Pin(15))
pwm.freq(5000)   # Frecuencia fija de 5 kHz
Vcc = 3.3        # Voltaje de salida del Pico (GPIO)

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
6