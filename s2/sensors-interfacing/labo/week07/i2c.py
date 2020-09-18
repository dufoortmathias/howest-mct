#pylint: skip-file
from RPi import GPIO as io
import time

delay = 0.002
up = 19
down = 26
sda = 27
scl = 22
adres = 0x38


class PCF8574:
    def __init__(self, SDA, SCL, address, btn_up, btn_down):
        self.sda = SDA
        self.scl = SCL
        self.__address = address
        self.__dot = 0


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
        
        # display buttons
        self.buttons = [btn_up, btn_down]
        # display cijfer
        self.cijfer = 0
        # io setup en adres doorklokken
        self.__setup()


    def write_outputs(self, data: int):
        #ack simuleren door 1 bit te writen
        pcf._PCF8574__writebit(1)
        #data, geinverteerd want display is een CA
        pcf._PCF8574__writebyte(~data)

    @property
    def dot(self):
        return self.__dot

    # om het puntje aan of uit te zetten
    @dot.setter
    def dot(self, value):
        self.__dot = value

    @property
    def address(self):
        return self.__address

    # om het adres van het device te wijzigen
    @address.setter
    def address(self, value):
        self.__address = value

    def __setup(self):
        io.setmode(io.BCM)
        io.setup(self.sda, io.OUT)
        io.setup(self.scl, io.OUT)
        for btn in self.buttons:
            io.setup(btn, io.IN, pull_up_down=io.PUD_UP)
            io.add_event_detect(
                btn, io.FALLING, self.btn_callback, bouncetime=200)


    def __start_conditie(self):
        io.output(self.sda, io.HIGH)
        time.sleep(delay)
        io.output(self.scl, io.HIGH)
        time.sleep(delay)
        io.output(self.sda, io.LOW)
        time.sleep(delay)
        io.output(self.scl, io.LOW)
        time.sleep(delay)

    def __stop_conditie(self):
        io.output(self.scl, io.HIGH)
        time.sleep(delay)
        io.output(self.sda, io.HIGH)
        time.sleep(delay)

    def __writebit(self, bit):
        #sda bitwaarde geven
        io.output(self.sda, bit)
        time.sleep(delay)
        #clock hoog
        io.output(self.scl, io.HIGH)
        time.sleep(delay)
        #clock laag na delay
        io.output(self.scl, io.LOW)
        time.sleep(delay)

    def __ack(self):
        # setup input + pullup van sda pin
        io.setup(self.sda, io.IN, pull_up_down=io.PUD_UP)
        # klok omhoog brengen
        io.output(self.scl, io.HIGH)
        time.sleep(delay)
        # sda pin inlezen: laag = OK
        status = io.input(self.sda) == io.LOW
        # setup output van sda pin
        io.setup(self.sda, io.OUT)
        # klok omlaag
        io.output(self.scl, io.LOW)
        time.sleep(delay)
        return status

    def __writebyte(self, byte):
        mask = 0x80
        for i in range(8):
            self.__writebit(byte & (mask >> i))

    def btn_callback(self, btn):
        if int(btn) == self.buttons[0]:  # up
            self.cijfer += 1
        else:  # down
            self.cijfer -= 1
        self.cijfer %= 10
        print(self.cijfer)


if __name__ == "__main__":
    try:
        pcf = PCF8574(sda, scl, adres, up, down)  # 0x38 = adres van de PCF8574A

        ### display test ###

        #startconditie
        pcf._PCF8574__start_conditie()

        #adres doorklokken + RW=0 om te schrijven
        pcf._PCF8574__writebyte((pcf._PCF8574__address << 1) | 0b00000000)

        while True:
            display_byte = pcf.numbers[pcf.cijfer] | pcf._PCF8574__dot << 7
            pcf.write_outputs(display_byte)

    except KeyboardInterrupt as e:
        pass
    finally:
        #ack simuleren door 1 bit te writen
        pcf._PCF8574__writebit(1) 
        #stopconditie
        pcf._PCF8574__stop_conditie()


        io.cleanup()
