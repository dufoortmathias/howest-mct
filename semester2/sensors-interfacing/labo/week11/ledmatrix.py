from RPi import GPIO as io
import time
import spidev


class Max7219:
    def __init__(self, ce=0):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 10**5
        self.init_max7219()

    def init_max7219(self):
        self.display_off()
        self.set_intensity(0x0)
        self.set_limit(7)
        self.test_matrix()
        self.display_on()

    def test_matrix(self):
        self.spi.writebytes([0xF, 1])
        time.sleep(0.5)
        self.spi.writebytes([0xF, 0])

    def set_intensity(self, value):
        self.spi.writebytes([0xA, value])

    def set_limit(self, value):
        self.spi.writebytes([0xB, value])

    def display_on(self):
        self.spi.writebytes([0xC, 1])

    def display_off(self):
        self.spi.writebytes([0xC, 0])

    def draw_rectangle(self):
        self.spi.writebytes([0x1, 0xFF])
        for i in range(0, 6):
            self.spi.writebytes([i+2, 0x81])
        self.spi.writebytes([0x8, 0xFF])

    def draw_rectangle_with_cross(self):
        self.spi.writebytes([0x1, 0xFF])  # 0b11111111 255
        mask = 0x81
        for i in range(0, 3):  # van rij 2 tot en met rij 4
            self.spi.writebytes(
                [i + 2, mask | 0x80 >> i + 1 | 0x01 << i + 1]) 
        for i in range(0, 3):  # van rij 5 tot en met rij 7
            self.spi.writebytes(
                [i + 5, mask | 0x10 << i | 0x08 >> i])

        self.spi.writebytes([0x8, 0xFF])  # 0b11111111 255

    def delete_matrix(self):
        for i in range(1, 9):
            self.spi.writebytes([i, 0x00])


    def draw_pixel(self, row, col):
        pass

    def clear_pixel(self, row, col):
        pass

    def toggle_pixel(self, row, col):
        pass


if __name__ == "__main__":
    max7219 = Max7219()
    try:
        max7219.delete_matrix()
        time.sleep(0.5)
        max7219.draw_rectangle()
        time.sleep(0.5)
        max7219.draw_rectangle_with_cross()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        #max7219.display_off()
        pass

