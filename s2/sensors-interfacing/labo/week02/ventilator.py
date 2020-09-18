#!/usr/bin/python3

import time
from RPi import GPIO


sensor_file = "/sys/bus/w1/devices/28-0317977998cd/w1_slave"
sensor = open(sensor_file, "r")
temp_gewenst = float(input("Geef de gewenste temp_curr op: "))
hysterese = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
motor = GPIO.PWM(21, 1000)


######

def read_temp():
    temp = 0
    with open(sensor_file, "r") as sensor:
        for i, line in enumerate(sensor):
            if i == 1: # 2de regel
                temp = float(line[line.find("t=")+2:])/1000.0
                print("Het is {0} C \t Verschil in temperatuur: {1}".format(temp, temp - temp_gewenst))
                return temp

def run():
    duty_cycle = 0
    motor.start(duty_cycle)
    try:
        while True:
            temp_curr = read_temp()
            temp_diff = temp_curr - temp_gewenst

            if duty_cycle == 0: # ventilator uitgeschakeld (temp_diff <= 2)
                if temp_diff >= 2 + hysterese/2:
                    duty_cycle = 30
            if duty_cycle == 30: # temp diff tussen 2 en 4
                if temp_diff <= 2 - hysterese/2:
                    duty_cycle = 0
                elif temp_diff >= 4 + hysterese/2:
                    duty_cycle = 50
            if duty_cycle == 50: # temp diff tussen 4 en 6
                if temp_diff <= 4 - hysterese/2:
                    duty_cycle = 30
                elif temp_diff >= 6 + hysterese/2:
                    duty_cycle = 100
            if duty_cycle == 100: # temp diff >= 6
                if temp_diff <= 6 - hysterese/2:
                    duty_cycle = 50
                                
            
            motor.ChangeDutyCycle(duty_cycle)
            print("motor cycle: {}".format(duty_cycle))

    except KeyboardInterrupt as e:
        print("\nProgramma gestopt.")
    finally:
        motor.stop()
        GPIO.cleanup()


run()