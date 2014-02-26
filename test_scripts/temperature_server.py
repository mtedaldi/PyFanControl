#! /usr/bin/python

# A simple Python command line tool to read temperature values
# from an MPC9808 integrated temperature sensor.
# by Marco Tedaldi, 19.2.2014
# GNU GPL V3 

import socket
import smbus
import sys
import getopt
import time 
# Use SMBus 1 ("0" in rev. 1 Boards) on the GPIO-Connector
bus = smbus.SMBus(1)

s = socket.socket()
host = socket.gethostname()
print host
port = 7777
s.bind((host, port))



# Enter the Address here that you have set on A0-A3
# Don't forget to add 0x18 because of preset bits
address = 0x19 # I2C address of MCP23017


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



s.listen(5)
while True:
  c, addr = s.accept()
  print 'Got a connection from', addr
  temperature = str(get_temperature(address)) + '\n'
  c.send(temperature)
  c.close()

