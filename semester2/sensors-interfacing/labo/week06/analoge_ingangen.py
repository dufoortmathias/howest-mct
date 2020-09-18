#pylint: skip-file
import spidev
import time
import RPi.GPIO as io


class MCP:
    def __init__(self, bus=0, device=0):
        # spidev object initialiseren
        self.spi = spidev.SpiDev()
        # open bus 0, device 0
        self.spi.open(bus, device)
        # stel klokfrequentie in op 100kHz
        self.spi.max_speed_hz = 10 ** 5

    def read_channel(self, ch):
        # commandobyte samenstellen
        channel = ch << 4 | 128
        # list met de 3 te versturen bytes
        bytes_out = [0b00000001, channel, 0b00000000]
        # versturen en 3 bytes terugkrijgen
        bytes_in = self.spi.xfer2(bytes_out)
        # meetwaarde uithalen
        byte1 = bytes_in[1]
        byte2 = bytes_in[2]
        result = byte1 << 8 | byte2
        # meetwaarde afdrukken
        if ch == 0:  # trimmer
            print(str(result) + "\t" +
                  format(value_to_voltage(result), '.2f') + " V")
            servo(result)
        elif ch == 1:  # ldr
            # ldr geeft hoge waardes bij weinig licht, dus 1023 - result om logische waarde te krijgen
            result = 1023 - result
            print(str(result) + "\t" +
                  format(value_to_percentage(result), '.2f') + " %")

    def close_spi(self):
        self.spi.close()


def value_to_voltage(waarde):
    return 3.3*(waarde / 1023.0)


def value_to_percentage(waarde):
    return (waarde/1023.0)*100


def value_to_angle(value):
    return (value / 1023.0) * 180


def servo(value):
    angle = value_to_angle(value)
    duty = angle / 18 + 2
    pwm.start(duty)
    time.sleep(1)


if __name__ == "__main__":
    io.setmode(io.BCM)
    io.setup(21, io.OUT)
    pwm = io.PWM(21, 50)
    pwm.start(0)
    channel = input("Which channel do you want to read? ")
    mcp = MCP()
    try:
        while(True):
            mcp.read_channel(int(channel))
    except ValueError as e:
        print("Please enter an integer.")
    except KeyboardInterrupt as e:
        print("quitting...")
    finally:
        mcp.close_spi()
        io.cleanup()
        pwm.stop()
