#pylint: skip-file
from RPi import GPIO
import time

led = 12

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)


def send_string(string):
    for i in string:
        byte = ord(i)
        send_byte(byte)

def send_byte(byte):
    #eerst moet de MSB verstuurd worden
    print("Sending byte: " + str(byte))
    
    mask = 0x80 # 128 of 0b1000 0000

    for i in range(8):
        mask = 0x80 >> i
        bitwaarde = byte & mask
        if bitwaarde > 0:
            GPIO.output(led, GPIO.HIGH)
            print("1")
        else:
            GPIO.output(led, GPIO.LOW)
            print("0")
        time.sleep(0.2)
        
    




if __name__ == '__main__':
    try:
        setup()
        string = input("Geef een string: ")
        send_string(string)
    except KeyboardInterrupt as e:
        print(e)
    finally:
        GPIO.cleanup()