# pylint: skip-file
from RPi import GPIO
import time


# variables
DS = 17
OE = 27
STCP = 22
SHCP = 5
MR = 6
up_btn = 23
down_btn = 24


# class
class Shiftregister:
    def __init__(self, ds_pin=DS, oe_pin=OE, stcp_pin=STCP, shcp_pin=SHCP, mr_pin=MR):
        self.ds_pin = DS
        self.oe_pin = OE
        self.stcp_pin = STCP
        self.shcp_pin = SHCP
        self.mr_pin = MR

        self.up_btn = up_btn
        self.down_btn = down_btn

        self.pins = [DS, OE, STCP, SHCP, MR]
        self.buttons = [up_btn, down_btn]

        A = 1 << 0
        B = 1 << 1
        C = 1 << 2
        D = 1 << 3
        E = 1 << 4
        F = 1 << 5
        G = 1 << 6
        H = 1 << 7  # H = decimal point

        self.numbers = [
            A | B | C | D | E | F,  # 0
            B | C,  # 1
            A | B | G | E | D,  # 2
            A | B | G | C | D,  # 3
            F | G | B | C,  # 4
            A | F | G | C | D,  # 5
            A | F | G | E | C | D,  # 6
            A | B | C,  # 7
            A | B | C | D | E | F | G,  # 8
            A | B | C | D | F | G,  # 9
            H  # DP
        ]
        self.cijfer = 0

        GPIO.setmode(GPIO.BCM)
        for i, pin in enumerate(self.pins):
            GPIO.setup(pin, GPIO.OUT)
        for i, btn in enumerate(self.buttons):
            GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(
                btn, GPIO.FALLING, self.btn_callback, bouncetime=200)

        GPIO.output(oe_pin, GPIO.LOW)
        GPIO.output(mr_pin, GPIO.HIGH)
        GPIO.output(stcp_pin, GPIO.HIGH)

    def write_bit(self, value):
        # puls shiftregister met 1 databit
        GPIO.output(self.ds_pin, not value)
        GPIO.output(self.shcp_pin, GPIO.HIGH)
        GPIO.output(self.shcp_pin, GPIO.LOW)

    def copy_to_storage_register(self):
        GPIO.output(self.stcp_pin, GPIO.HIGH)
        GPIO.output(self.stcp_pin, GPIO.LOW)

    def write_one_byte(self, data_byte):
        mask = 0x80
        for i in range(0, 8):
            self.write_bit(data_byte & (mask >> i))
        self.copy_to_storage_register()

    def add_dot(self):
        self.write_one_byte(
            self.numbers[self.cijfer] | self.numbers[10])

    
    def output_enabled(self, bool):
        if bool:
            GPIO.output(self.oe_pin, GPIO.HIGH)
        else:
            GPIO.output(self.oe_pin, GPIO.LOW)

    def btn_callback(self, btn):
        if int(btn) == 23:  # up
            self.cijfer += 1
        else:  # down
            self.cijfer -= 1
        self.cijfer %= 10


# main
if __name__ == "__main__":
    try:
        sr = Shiftregister(DS, OE, STCP, SHCP, MR)
        try:
            cijfer = int(input("Please input a number between 0 and 9:  "))
        except:
            print("You haven't entered a number. Setting to 0")
            cijfer = 0
        if cijfer in range(0, 10):
            sr.cijfer = cijfer
            while(True):
                sr.write_one_byte(sr.numbers[sr.cijfer])
                sr.copy_to_storage_register()
        else:
            print(cijfer)

    except KeyboardInterrupt as e:
        "\nQuitting..."
    finally:
        GPIO.cleanup()
