
class PCF8574:
    def __init__(self, SDA, SCL, address, btn_up, btn_down):
        self.sda = SDA
        self.scl = SCL
        self.__address = address
        self.__setup()

    def write_outputs(self, data: int):
        address_write = self.address << 1
        data = data & 0xFF
        self.__start_conditie()
        self.__writebyte(address_write)
        self.__ack()
        self.__writebyte(data)
        self.__ack()
        self.__stop_conditie()

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

    def __start_conditie(self):
        io.output(self.sda, io.HIGH)
        io.output(self.scl, io.HIGH)
        io.output(self.sda, io.LOW)
        io.output(self.scl, io.LOW)

    def __stop_conditie(self):
        io.output(self.sda, io.LOW)
        io.output(self.scl, io.LOW)
        io.output(self.scl, io.HIGH)
        io.output(self.sda, io.HIGH)

    def __writebit(self, bit):
        #sda bitwaarde geven
        io.output(self.sda, bit)
        #clock hoog
        io.output(self.scl, io.HIGH)
        #clock laag na delay
        io.output(self.scl, io.LOW)
        io.output(self.sda, io.LOW)

    def __ack(self):
        # setup input + pullup van sda pin
        io.setup(self.sda, io.IN, pull_up_down=io.PUD_UP)
        # klok omhoog brengen
        io.output(self.scl, io.HIGH)
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

    @staticmethod
    def search_addresses(SDA, SCL):
        addresses = []
        i2cdev = Pcf8574(SDA, SCL)
        for i in range(0x20, 0x80, 2):
            i2cdev.address = i << 1
            i2cdev.__start_conditie()
            i2cdev.__writebyte(i)
            if i2cdev.__ack():
                addresses.append(i)
                i2cdev.__stop_conditie()
        return addresses
