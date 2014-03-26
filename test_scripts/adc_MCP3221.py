#! /usr/bin/python3

# A simple Python command line tool to read voltage values
# from an MCP3221 ADC.
# by Marco Tedaldi, 18.3.2014
# License: http://opensource.org/licenses/MIT 

import quick2wire.i2c as i2c
import re
import time
import sys

# Read the temperature from the given address
def get_value(bus, addr):
# Read a 16bit word from register 0x05
    hi, lo = bus.transaction(i2c.reading(addr, 2))[0]
    value = (hi << 8) | lo
    return value


# the "Main" function which just calls get_temperature and prints the results to stdout
def main():
    i2c_bus = 1  
    address = 0x4D
    with i2c.I2CMaster(i2c_bus) as bus:
        while True:
            try:
                voltage = 0
                for i in range(0, 8):
                    voltage = voltage + (get_value(bus, address) / 8)
                print(int(voltage))
                time.sleep(0.2)
            except KeyboardInterrupt:
                print("received ctrl+c, terminating")
                sys.exit()


# calling the "Main" function
if __name__ == "__main__":
    main();

