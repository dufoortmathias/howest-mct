#!/usr/bin/python3

from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
motor = GPIO.PWM(21, 1000)
motor.start(100)

try:
    while True:
        duty_cycle = int(input("Geef de gewenste duty cycle op: "))
        motor.ChangeDutyCycle(duty_cycle)
        time.sleep(1)
except KeyboardInterrupt as e:
    print("    interrupt")
finally:
    motor.stop()
    GPIO.cleanup()
