#pylint: skip-file
from RPi import GPIO
import time
import serial 



knop = 12
knop2 = 16

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(knop, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(knop2, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(knop, GPIO.FALLING, drukKnop, bouncetime=100)
    GPIO.add_event_detect(knop2, GPIO.FALLING, drukKnop2, bouncetime=100)

def drukKnop(pin):
    print("1")
    ser.write(b'sensor1')

def drukKnop2(pin):
    print("1")
    ser.write(b'sensor2')

setup()

ser = serial.Serial('/dev/serial0') # open serial port
print(ser.name)     # check which port was used
while True:
    print(ser.readline())
ser.close()         # close port

