#! /usr/bin/python3

# A simple Python command line tool to read volate values
# from an MCP3221 ADC.
# (c) by Marco Tedaldi, 18.3.2014


import quick2wire.i2c as i2c
import re
import time
import sys


class gpio:
    iodir_register = 0x00
    gpio_register = 0x0A

    def __init__(self):
        self.busnr = 1
        return

    # Initialize the bus object.
    # This should only be done if the bus has not been initialized externally.
    def businit(self, busnr=1):
        self.bus = i2c.I2CMaster(busnr)
        return self.bus


    # Set the bus object for the i2c device
    def set_bus(self, bus):
        self.bus = bus
        return


    # Return the bus object for the i2c device
    def get_bus(self):
        return self.bus

    # Set the address of the I2C device
    def set_address(self, addr):
        self.addr = addr
        return

    # Return the address set for the I2C device 
    def get_address(self):
        return self.addr


    # Set the IO Direction Register (Default 0b1111 1111, 1=input, 0=output)
    def set_ioDirectionReg(self, ioDir):
        self.ioDir = ioDir
        self.__setReg(iodir_register, ioDir)
        return ioDir


    # Return the Value of the IO Direction Register in the MCP23009
    def get_ioDirectionReg(self):
        self.ioDir = self.__getReg(iodir_register)
        return self.ioDir


    # Set the direction of a single IO-line
    def set_ioLineDirection(self, line, direction):
        lineMask = 2**line
        if direction == 0:
            self.ioDir = self.ioDir & !lineMask
        else:
            self.ioDir = self.ioDir | lineMask
        self.__setReg(iodir_register, self.ioDir)
        return self.ioDir





    def __setReg(self, register, value):
        self.bus.transaction(i2c.writing_bytes(self.addr, regsiter, value))
        return



    # Method for internal use, get the value of a register
    def __getReg(self, register):
        reg_value = self.bus.transaction(
            i2c.writing_bytes(self.addr, register),
            i2c.reading(self.addr, 1))
        return reg_value[0][0]






# the "Main" function which just calls get_temperature and prints the results to stdout
def main():
    i2c_bus = 1  
    address = 0x20
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

