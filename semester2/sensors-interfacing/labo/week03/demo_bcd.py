#pylint: skip-file
from RPi import GPIO
import time

bits = [1,2,4,8]
bcd_pinnen = [4,17,27,22]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in bcd_pinnen:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

def lees_bcd_code():
    #arr = []
    arr = [True for i in range(4)]  # debug
    # for pin in bcd_pinnen:
    #     arr.append(inverteer(GPIO.input(pin)))
    for i in arr:
        print(i)
    for i, value in enumerate(arr):
        arr[i] = value << i
    print(arr)
    return naar_dec(arr)


def knipperLicht():
    GPIO.output(led, 1)
    time.sleep(0.5)
 

def inverteer(bit):
    return int(not bit)

def naar_dec(arr):
    return arr[0] | arr[1] | arr[2] | arr[3]
    # sum = 0
    # for i in arr:
    #     sum += i
    # return sum

if __name__ == "__main__":
    try:
        setup()
        print(lees_bcd_code())
    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("\nEnded")
        GPIO.cleanup()
