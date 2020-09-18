from smbus import SMBus
import time

i2c = SMBus()  # init library
i2c.open(1)  # open bus 1


class MPU6050:
    def __init__(self, address):
        self.addr = address
        self.setup()

    def setup(self):
        # schaalfactor accelerometer
        self.__write_byte(0x1C, 0x00)
        # schaalfactor gyroscoop
        self.__write_byte(0x1B, 0x00)
        # sensor uit slaapstand
        self.__write_byte(0x6B, 0x01)

    def print_data(self):
        print("***")
        print('De temperatuur is {}°C'.format(self.read_temp()))
        accel = self.read_accel()
        print('Accel: x = {0}, y = {1}, z = {2}'.format(
            accel[0], accel[1], accel[2]))
        gyro = self.read_gyro()
        print('Gyro : x = {0}°/s, y = {1}°/s, z = {2}°/s'.format(
            gyro[0], gyro[1], gyro[2]))
        print()

    @staticmethod
    def combine_bytes(msb, lsb):
        value = msb << 8 | lsb
        if value & 0x8000:
            value -= 65536  # 2^n, n=16
        return value

    def read_temp(self):
        values = self.__read_data(0x41, 2)
        return round(values[0] / 340 + 36.53, 2)

    def read_accel(self):
        values = self.__read_data(0x3B, 6)
        for i in range(len(values)):
            values[i] = round(values[i] / 16384, 2)
        return values

    def read_gyro(self):
        values = self.__read_data(0x43, 6)
        for i in range(len(values)):
            values[i] = round(values[i] / 250, 2)
        return values

    def __write_byte(self, register, value):
        i2c.write_byte_data(self.addr, register, value)

    def __read_data(self, register, count):
        arr = i2c.read_i2c_block_data(self.addr, register, count)
        values = []
        for i in range(0, count, 2):
            byte = self.combine_bytes(arr[i], arr[i+1])
            values.append(byte)
        return values


if __name__ == "__main__":
    try:
        mpu = MPU6050(0x68)
        while True:
            mpu.print_data()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('quitting')
    finally:
        i2c.close()
