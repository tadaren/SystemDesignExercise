import smbus


class Sensor:

    def __init__(self):
        self.i2c = smbus.SMBus(1)
        self.i2c_addr = 0x45

        self.i2c.write_byte_data(self.i2c_addr, 0x21, 0x30)

    def get_humid(self):
        return self.get()[1]

    def get(self):
        self.i2c.write_byte_data(self.i2c_addr, 0xE0, 0x00)
        data = self.i2c.read_i2c_block_data(self.i2c_addr, 0x00, 6)
        temp = temp_changer(data[0], data[1])
        humid = humid_changer(data[3], data[4])
        return temp, humid


def temp_changer(msb, lsb):
    mlsb = ((msb << 8) | lsb)
    return -45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1)


def humid_changer(msb, lsb):
    mlsb = ((msb << 8) | lsb)
    return 100 * int(str(mlsb), 10) / (pow(2, 16) - 1)
