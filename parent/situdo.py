import time
import smbus
import datetime


def tempChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)                                             # P1
    return (-45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1))            # P2


def humidChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)
    return (100 * int(str(mlsb), 10) / (pow(2, 16) - 1))


i2c = smbus.SMBus(1)
i2c_addr = 0x45                                                           # P3

i2c.write_byte_data(i2c_addr, 0x21, 0x30)                                 # P4
time.sleep(0.5)

with open('result.csv', 'a') as file:
    while 1:
        # P5
        i2c.write_byte_data(i2c_addr, 0xE0, 0x00)
        data = i2c.read_i2c_block_data(
            i2c_addr, 0x00, 6)                     # P6

        temp = tempChanger(data[0], data[1])
        humid = humidChanger(data[3], data[4])
        print(str('{:.4g}'.format(temp)) + "C")
        print(str('{:.4g}'.format(humid)) + "%")
        print("------")

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{now}, {temp:.4g}, {humid:.4g}\n')
        file.flush()

        time.sleep(60)
