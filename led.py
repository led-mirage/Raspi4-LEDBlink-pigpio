"""
Raspberry Pi Lチカサンプル
pigpioライブラリ使用

Copylight (c) 2023 led-mirage
"""

import pigpio
import time

LED_PIN = 26

pi = pigpio.pi()
duty = 10 # 0-255

try:
    while True:
        pi.set_PWM_dutycycle(LED_PIN, duty)
        time.sleep(1)
        pi.set_PWM_dutycycle(LED_PIN, 0)
        time.sleep(1)
except KeyboardInterrupt: # Ctrl+C
    pass

pi.set_PWM_dutycycle(LED_PIN, 0)
pi.stop()
