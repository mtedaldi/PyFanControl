#!/usr/bin/python3
#
# Functions to write data to a Display connected by i2c
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch>, 2014
# License: MIT, http://opensource.org/licenses/MIT
#

import time
import quick2wire.i2c as i2c

#Bus Nr and Address
bus_nr = 1 # Use Bus number 1 (on Raspi Rev 1, bus 0 is preferable)
address = 0x3E


class i2c_display:
    def __init__(self, d_bus, d_address):
        self.address = d_address
        self.bus = d_bus
        self.write_data(0x00, 0x38) # I don'6 know if this even makes sense. It's from the example!
        self.write_data(0x00, 0x39) # Function Set, 8bit, 2lines, NoDoubleHeight, InstructionTable=1
        self.write_data(0x00, 0x14) # Bias=0 (1/5), AdjIntOsc=4
        self.write_data(0x00, 0x74) # Set Contrast bits 3..0 to 4
        self.write_data(0x00, 0x54) # Icon=off, booster=on, Contrast bits 5+4 = 0
        self.write_data(0x00, 0x6F) # Switch on follower circuit and set ratio to 7
        self.write_data(0x00, 0x38) # Function Set, 8bit, 2lines, NoDoubleHeight, InstructionTable=0
        self.write_data(0x00, 0x0C) # Cursor on
        return


    def write_data(self, rs, command):
        time.sleep(0.01) # Wait 10ms before writing.
                         # Since the used controler does not allow read acces on i2c, we can't poll
                         # the busy flag.
        self.bus.transaction(i2c.writing_bytes(self.address, rs, command))
        return



# Name: clear
# Function: Write the command "0x01" to the display which clears the display
    def clear(self):
        self.write_data(0x00, 0x01)
        return


# Name: write_char
# Function: Write a character to the current position
    def write_char(self, character):
        self.bus.transaction(i2c.writing_bytes(self.address, 0x40, ord(character)))
        return


# Name write_xy
# Function: Write a character to a given position in DDRAM
    def write_xy(self, col, line, character):
        if line == 1:
            command = (col & 0x3F) | 0xC0
        else:
            command = (col & 0x3F) | 0x80
        self.bus.transaction(i2c.writing_bytes(self.address, 0x00, command))
        self.write_char(character)
        return



# Name: write_string
# Function: Write a string of characters to the display
    def write_string(self, line, text):
        if line == 1:
            start_addr = 0x40
        else:
            start_addr = 0x00
        start_addr = start_addr | 0x80
        self.bus.transaction(i2c.writing_bytes(self.address, 0x00, start_addr))
        for char in text:
            self.write_char(char)
        return


    def write_cgchar(self, pos, data):
        cgaddr = pos & 0x07
        cgaddr = (cgaddr << 3) | 0x40
        time.sleep(0.1)
        self.bus.transaction(i2c.writing_bytes(self.address, 0x00, 0x38)) # Function Set, 8bit, 2lines, NoDoubleHeight, InstructionTable=0
        time.sleep(0.1)
        self.bus.transaction(i2c.writing_bytes(self.address, 0x00, cgaddr)) # select CGRAM address
        time.sleep(0.1)
        for datum in data:
            self.bus.transaction(i2c.writing_bytes(self.address, 0x40, datum)) # Write data, byte by byte (normally 8)
        self.bus.transaction(i2c.writing_bytes(self.address, 0x00, 0x80)) # return to DDRAM



# Name: Main
# The main program
def main():
    cust_char = [0x00, 0x10, 0x08, 0x04, 0x02, 0x01, 0x00, 0x00]
#    bus = smbus.SMBus(bus_nr)
    with i2c.I2CMaster(bus_nr) as bus:
        disp = i2c_display(bus, address)
        disp.clear()
        disp.write_cgchar(0, cust_char)
        time.sleep(0.1)
        disp.write_string(0, "Test")
        time.sleep(0.1)
        disp.write_xy(15, 0, "A")
        time.sleep(0.1)
        disp.write_xy(14, 0, chr(0x00))
        while 1:
            response = disp.get_status()
            print(response)
        return


if __name__ == "__main__":
        main();


