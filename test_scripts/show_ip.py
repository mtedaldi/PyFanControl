#!/usr/bin/python
#
# Python Program to display the IP-Address on the i2c display
# (c) Marco Tedaldi, 2014

import i2c_display
import get_ip
import smbus

bus_nr = 1
address = 0x3E

def main():
    ip = get_ip.get_ip()
    bus = smbus.SMBus(bus_nr)
    i2c_display.init_display(bus, address)
    i2c_display.display_write_string(bus, address, 0, ip)
    content = "Hallo Martin"
    i2c_display.display_write_string(bus, address, 1, content)
    return



if __name__ == "__main__":
        main();


