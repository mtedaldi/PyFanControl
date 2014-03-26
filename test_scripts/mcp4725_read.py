#! /usr/bin/python

# A simple Python command line tool to read temperature values
# from an MPC9808 integrated temperature sensor.
# by Marco Tedaldi, 19.2.2014
# License: MIT http://opensource.org/licenses/MIT

import smbus
import sys
import getopt
import time
# Use SMBus 1 ("0" in rev. 1 Boards) on the GPIO-Connector
bus = smbus.SMBus(1)


# Enter the Address here that you have set on A0-A3
# Don't forget to 0x18 because of preset bits
address = 0x60 # I2C address of MCP23017

#for i in range(0,4096):
    #lo = i & 0x00FF
    #hi = (i & 0x0F00) >> 8
    #print i, hi, lo
    #bus.write_byte_data(address, hi, lo)
#        time.sleep(0.01)


data = bus.read_byte(address)
print hex(data)

# Read the temperature from the given address
def get_temperature(addr):
# Read a 16bit word from register 0x05
  temp = bus.read_word_data(addr,0x05)
# We need to byte swap and shift the output
# We throw away th upper nibble which contains status und sign!
  hi = ( temp & 0x000F ) << 4
# we take the "lower" byte which contains also contains the fractionals in the lower nibble
  lo = ( temp & 0xFF00 ) >> 8
  lo = lo / 16.0
  temp = hi + lo
 
  return temp


# the "Main" function which just calls get_temperature and prints the results to stdout
def main():
  temperature = get_temperature(address)
  print temperature
  return

# calling the "Main" function
#main();


