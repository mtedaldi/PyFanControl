#!/usr/bin/python
#
# Functions to write data to a Display connected by i2c

import smbus

#Bus Nr and Address
bus_nr = 1
address = 0x3E


# Name: clear_display
# Function: Write the command "0x01" to the display which clears the display
def clear_display(bus, address):
    bus.write_byte_data(address, 0x00, 0x01)
    print "cleared"
    return


# Name: init_display
# Function: Initialize the Display registers to default values
def init_display(bus, address):
    bus.write_byte_data(address, 0x00, 0x38)
    bus.write_byte_data(address, 0x00, 0x39) # Function Set, 8bit, 2lines, NoDoubleHeight, InstructionTable=1
    bus.write_byte_data(address, 0x00, 0x14) # Bias=0 (1/5), AdjIntOsc=4
    bus.write_byte_data(address, 0x00, 0x74) # Set Contrast bits 3..0 to 4
    bus.write_byte_data(address, 0x00, 0x54) # Icon=off, booster=on, Contrast bits 5+4 = 0
    bus.write_byte_data(address, 0x00, 0x6F) # Switch on follower circuit and set ratio to 7
    bus.write_byte_data(address, 0x00, 0x0C) # Cursor on
    print "initialized"
    clear_display(bus, address)
    return

# Name: display_write_char
# Function: Write a character to the current position
def display_write_char(bus, address, character):
    bus.write_byte_data(address, 0x40, character)
    print '"' + chr(character) + '" written'
    return

# Name: display_write_string
# Function: Write a string of characters to the display
def display_write_string(bus, address, line, text):
    if line == 1:
        start_addr = 0x40
    else:
        start_addr = 0x00
    start_addr = start_addr | 0x80
    bus.write_byte_data(address, 0x00, start_addr)
    for char in text:
        display_write_char(bus, address, ord(char))
    return

# Name: Main
# The main program
def main():
    bus = smbus.SMBus(bus_nr)
    init_display(bus, address)
#    display_write_char(bus, address,ord("A"))
    display_write_string(bus, address, 0, "Test")
    return


if __name__ == "__main__":
        main();


