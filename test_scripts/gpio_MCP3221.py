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

    def __init__(self, busnr=1, address=0x20):
        self.addr = address
        self.bus = self.bus = i2c.I2CMaster(busnr)
        self.ioDir = self.__getReg(iodir_register)
        self.ioData = self.__getReg(gpio_register)
        return



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
            self.ioDir = self.ioDir & ~lineMask
        else:
            self.ioDir = self.ioDir | lineMask
        self.__setReg(iodir_register, self.ioDir)
        return self.ioDir

     # Set the GPIO-register
    def set_gpio(self, ioData):
        self.ioData = ioData
        self.__setReg(gpio_register, ioData)
        return ioData

    # Get the state of the gpio pins
    def get_gpio(self):
        self.ioData = self.__getReg(gpio_register)
        return self.ioData

    def set_gpioLine(self, line, state):
        lineMask = 2**line
        if state == 0:
            self.ioData = self.ioData & ~lineMask
        else:
            self.ioData = self.ioData | lineMask
        self.__setReg(gpio_register, self.ioData)
        return self.ioData





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
    io = gpio(i2c_bus, address)
    io.set_ioDir(0x00)
    gpio = 0x00
    while True:
        try:
            io.set_gpio(gpio)
            gpio = ~gpio
            print(gpio)
            time.sleep(0.2)
        except KeyboardInterrupt:
            print("received ctrl+c, terminating")
            sys.exit()


# calling the "Main" function
if __name__ == "__main__":
    main();

