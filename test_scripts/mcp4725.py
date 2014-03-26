#! /usr/bin/python

# A simple Python command line tool to vrite voltage 
# values to an MCP4725 DAC.
# by Marco Tedaldi, 24.2.2014
# License: MIT, http://opensource.org/licenses/MIT

import smbus
import sys
import getopt
import time

# Use SMBus 1 ("0" in rev. 1 Boards) on the GPIO-Connector
bus_nr = 1


# Enter the Address here that you have set on A0
# Don't forget to 0x60 because of preset bits
device_address = 0x60 # I2C address of MCP23017

def sanitize_dac_value(value):
    if (value > 4095):
        value = 4095
    if (value < 0):
        value = 0
    return value
    

def dac_write(bus, address, value):
    lo = int(value & 0x00FF)
    hi = int((value & 0x0F00) >> 8)
    bus.write_byte_data(address, hi, lo)


def dac_write_list(bus, address, vs):
    bus.write_i2c_block_data(address, vs[0], vs[1:])
        

def format_value_list(values):
    values_new = []
    for v in values:
        values_new.append((v & 0x0F00) >> 8)
        values_new.append(v & 0x00FF)
    return values_new



def dac_set_default(bus, address, value):
    value = sanitize_dac_value(value)
    value = value << 4
    bus.write_word_data(int(address), 0x30, value)

def generate_ramp(bus, address, min_value, max_value):
    for i in range(min_value, max_value):
        dac_write(bus, address, i)






# the "Main" function which just calls the generate ramp function 
def main(bus_n, dev_addr):
    bus = smbus.SMBus(bus_n)
    val_min = 0
    val_max = 16
    #voltage_vals = range(val_min, val_max)
    voltage_vals=[]
    for i in range(val_min, val_max):
        voltage_vals.append(i*64)
    print voltage_vals
    voltage_vals = format_value_list(voltage_vals)
    print voltage_vals
    while True:
        dac_write_list(bus, dev_addr, voltage_vals)

    #while True:
        #generate_ramp(bus, dev_addr, val_min, val_max)

# calling the "Main" function
if __name__ == "__main__":
    main(bus_nr, device_address);


