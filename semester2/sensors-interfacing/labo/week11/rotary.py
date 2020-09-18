#pylint: skip-file
from RPi import GPIO as io
import time

class Rotary:
    def __init__(self, clk=16, dt=20, sw=24):
        self.dt = dt
        self.clk = clk
        self.sw = sw

        self.clkLastState = 0
        self.counter = 0
        self.switchState = 0

        self.setup_pins()

    def setup_pins(self):
        io.setmode(io.BCM)
        io.setup(self.dt, io.IN, pull_up_down=io.PUD_UP)
        io.setup(self.clk, io.IN, pull_up_down=io.PUD_UP)
        io.setup(self.sw, io.IN, pull_up_down=io.PUD_UP)

        io.add_event_detect(self.clk, io.BOTH, self.rotation_decode, 1)
        # io.add_event_detect(self.dt, io.BOTH, self.rotation_decode, 1)
        io.add_event_detect(self.sw, io.FALLING, self.pushed, 200)


    def rotation_decode(self, pin):
        dt_value = io.input(self.dt)
        clk_value = io.input(self.clk)
        
        if clk_value != self.clkLastState and clk_value == False:
            if dt_value != clk_value:
                print("Rechts")
                self.counter += 1
            else:
                print("Links")
                self.counter -= 1
            print(self.counter)
        self.clkLastState = clk_value

    def pushed(self, sw):
        print("Druk")

if __name__ == "__main__":
    rotary = Rotary(16, 20, 24)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
