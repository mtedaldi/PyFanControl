#!/usr/bin/python
#
# Functions to write data to a Display connected by i2c

import smbus

#Bus Nr and Address
bus_nr = 1
address = 0x20


# Name: clear_display
# Function: Write the command "0x01" to the display which clears the display
def clear_display(bus, address):
    bus.write_byte_data(address, 0x00, 0x01)
    return


# Name: init_display
# Function: Initialize the Display registers to default values
def init_display(bus, address):
    bus.write_byte_data(address, 0x00, 0x39) # Function Set, 8bit, 2lines, NoDoubleHeight, InstructionTable=1
    bus.write_byte_data(address, 0x00, 0x14) # Bias=0 (1/5), AdjIntOsc=4
    bus.write_byte_data(address, 0x00, 0x74) # Set Contrast bits 3..0 to 4
    bus.write_byte_data(address, 0x00, 0x54) # Icon=off, booster=on, Contrast bits 5+4 = 0
    bus.write_byte_data(address, 0x00, 0x6F) # Switch on fallower circuit and set ratio to 7
    bus.write_byte_data(address, 0x00, 0x0C) # Cursor on
    clear_display(bus, address)
    return

# Name: display_write_char
# Function: Write a character to the current position
def display_write_char(bus, address, character):


