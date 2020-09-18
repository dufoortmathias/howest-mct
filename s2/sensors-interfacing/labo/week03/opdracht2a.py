#pylint: skip-file
from RPi import GPIO
import time
bcd_pinnen = [5, 17, 27, 22]
witte_led = 20
rode_led = 16
rode_led2 = 21
knop = 12
knop2 = 18
bcd = False # False als we werken zonder bcd teller
rood = False # als rood == False, knipper wit licht

sensor_file = "/sys/bus/w1/devices/28-0317977998cd/w1_slave"
#sensor_file = "./test" # om de temperatuur te testen zonder temperatuursensor te moeten aansluiten
sensor = open(sensor_file, "r")

def setup():
    GPIO.setmode(GPIO.BCM)
    if bcd:
        for pin in bcd_pinnen:
            GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(witte_led, GPIO.OUT)
    GPIO.setup(rode_led, GPIO.OUT)
    GPIO.setup(rode_led2, GPIO.OUT)
    GPIO.setup(knop, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(knop2, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(knop, GPIO.FALLING, call_back_knop_event, bouncetime=100)
    GPIO.add_event_detect(knop2, GPIO.FALLING, print_temp, bouncetime=100)


def print_temp(pin):
    with open(sensor_file, "r") as sensor:
        for i, line in enumerate(sensor):
            if i == 1: # 2de regel
                temp = float(line[line.find("t=")+2:])/1000.0
                print("Het is {0} C".format(temp))

def call_back_knop_event(pin): # knop ingedrukt
    global rood
    rood = True 
    for i in range(1): # 20 seconden
        GPIO.output(rode_led, GPIO.HIGH)
        GPIO.output(rode_led2, GPIO.LOW)
        time.sleep(0.25)
        GPIO.output(rode_led, GPIO.LOW)
        GPIO.output(rode_led2, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(rode_led, GPIO.HIGH)
        GPIO.output(rode_led2, GPIO.LOW)
        time.sleep(0.25)
        GPIO.output(rode_led, GPIO.LOW)
        GPIO.output(rode_led2, GPIO.HIGH)
        time.sleep(0.25)
    GPIO.output(rode_led2, GPIO.LOW)
    rood = False



def lees_bcd_code():
    if bcd: # als we werken met een bcd teller
        num = 0
        for index, value in enumerate(bcd_pinnen):
            bit = not GPIO.input(value)
            num |= bit << index
        return num
    else: # anders vaste waarde
        return 1


def knipperLicht():
    n = lees_bcd_code()
    GPIO.output(witte_led, 1)
    time.sleep(n * 0.5)
    GPIO.output(witte_led, 0)
    time.sleep(n * 0.5)

setup()
if __name__ == '__main__':
    try:
        while True:
            if not rood:
                knipperLicht()
            time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
    finally:
        GPIO.cleanup()
