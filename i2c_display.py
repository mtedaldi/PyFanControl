#!/usr/bin/python
#
# Functions to write data to a Display connected by i2c

import smbus

#Bus Nr and Address
bus_nr = 1
address = 0x3E


class i2c_display:
    def __init__(self, d_bus, d_address):
        self.address = d_address
        self.bus = d_bus
        self.bus.write_byte_data(self.address, 0x00, 0x38)
        self.bus.write_byte_data(self.address, 0x00, 0x39) # Function Set, 8bit, 2lines, NoDoubleHeight, InstructionTable=1
        self.bus.write_byte_data(self.address, 0x00, 0x14) # Bias=0 (1/5), AdjIntOsc=4
        self.bus.write_byte_data(self.address, 0x00, 0x74) # Set Contrast bits 3..0 to 4
        self.bus.write_byte_data(self.address, 0x00, 0x54) # Icon=off, booster=on, Contrast bits 5+4 = 0
        self.bus.write_byte_data(self.address, 0x00, 0x6F) # Switch on follower circuit and set ratio to 7
        self.bus.write_byte_data(self.address, 0x00, 0x0C) # Cursor on
        return



# Name: clear
# Function: Write the command "0x01" to the display which clears the display
    def clear(self):
        self.bus.write_byte_data(self.address, 0x00, 0x01)
        return


# Name: write_char
# Function: Write a character to the current position
    def write_char(self, character):
        self.bus.write_byte_data(self.address, 0x40, ord(character))
        return

# Name: write_string
# Function: Write a string of characters to the display
    def write_string(self, line, text):
        if line == 1:
            start_addr = 0x40
        else:
            start_addr = 0x00
        start_addr = start_addr | 0x80
        self.bus.write_byte_data(self.address, 0x00, start_addr)
        for char in text:
            self.write_char(char)
        return

# Name: Main
# The main program
def main():
    bus = smbus.SMBus(bus_nr)
    disp = i2c_display(bus, address)
    disp.clear_display()
    disp.write_string(0, "Test")
    return


if __name__ == "__main__":
        main();


