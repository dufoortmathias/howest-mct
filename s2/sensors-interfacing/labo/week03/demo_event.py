#pylint: skip-file

from RPi import GPIO
import time
knop = 19
led = 13


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(knop, GPIO.IN, GPIO.PUD_UP)
    GPIO.output(led, 0)
    GPIO.add_event_detect(knop, GPIO.BOTH, bouncetime=1)
    GPIO.add_event_callback(knop, call_back_knop_event)

# polling = slechte manier:
def lees_knop_polling():
    pressed = not GPIO.input(knop)
    GPIO.output(led, pressed)
    print(pressed)

# betere manier:
def lees_knop_event():
    if GPIO.event_detected(knop):
        GPIO.output(led, 1)
        print("er is op de knop gedrukt")
    else:
        GPIO.output(led, 0)


def call_back_knop_event(pin):
    if GPIO.event_detected(knop):
        print("er is op de knop gedrukt")
        GPIO.output(led, 1)

        

if __name__ == '__main__':
    try:
        setup()
        while True:
            # lees_knop_event()
            # lees_knop_polling()
            time.sleep(0.5)
    except KeyboardInterrupt as e:
        print(e)
    finally:
        GPIO.cleanup()
