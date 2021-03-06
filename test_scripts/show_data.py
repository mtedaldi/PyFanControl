#!/usr/bin/python
# Python program that reads the temperature and displays it on the display
#
# (c) Marco Tedaldi, 2014

import i2c_display
import get_ip
import smbus
import temperature

bus_nr = 1
displ_addr = 0x3E
temp_addr = 0x19

def main():
    ip = get_ip.get_ip()
    bus = smbus.SMBus(bus_nr)
    i2c_display.init_display(bus, displ_addr)
    i2c_display.display_write_string(bus, displ_addr, 0, ip)
    temp = temperature.get_temperature(bus, temp_addr)
    line2 = "T: " + str(temp) + "C"
    i2c_display.display_write_string(bus, displ_addr, 1, line2)
    return



if __name__ == "__main__":
        main();


