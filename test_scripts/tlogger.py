#! /usr/bin/python

# A simple Python command line tool to read temperature values
# from an MPC9808 integrated temperature sensor and write them
# to a file every second
# by Marco Tedaldi, 19.2.2014
# License: MIT, http://opensource.org/licenses/MIT

import smbus
import sys
import getopt
import time
# Use SMBus 1 ("0" in rev. 1 Boards) on the GPIO-Connector
# bus = smbus.SMBus(1)


# Enter the Address here that you have set on A0-A3
# Don't forget to add 0x18 because of preset bits
# address = 0x19 # I2C address of MCP23017


# Read the temperature from the given address
def get_temperature(bus, addr):
# Read a 16bit word from register 0x05
  temp = bus.read_word_data(addr,0x05)
# We need to byte swap and shift the output
# We throw away th upper nibble which contains status und sign!
  hi = ( temp & 0x000F ) << 4
# we take the "lower" byte which contains also contains the fractionals in the lower nibble
  sign = (temp & 0x0010) # Sign of the temperature
  lo = ( temp & 0xFF00 ) >> 8
  lo = lo / 16.0
  temp = hi + lo
  if sign <> 0: # If the temperature is <0
      temp = temp - 256 # We have to fix the value thanks to 2s complement
  return temp


# the "Main" function which just calls get_temperature and prints the results to stdout
def main():
    address = 0x18
    bus = smbus.SMBus(1)
    try:
        n = int(sys.argv[1])
    except:
        print("Missing argument!\n")
        print("Usage:")
        print("    " + str(sys.argv[0]) + " n\n")
        print("    n = the number of values to record at 1s intervals")
        sys.exit()
    try:
        starttime = time.time()
        print("Temperature; time; Start time ; "+ str(starttime))
        for i in range(n):
            temperature = get_temperature(bus, address)
#            temperature2 = get_temperature(bus, 0x19)
            timeelapsed = time.time() - starttime
<<<<<<< HEAD
            print(str(temperature) + " ; " + str(timeelapsed))
            time.sleep(0.9977)
=======
            print(str(temperature) + ";" + str(timeelapsed))
            time.sleep(0.995)
>>>>>>> edd4d2de515e9b254fc72dead28d858688347df8
    except KeyboardInterrupt:
        sys.stderr.write("\nReceived ctrl+c, will terminate\n")
        sys.exit()

# calling the "Main" function
if __name__ == "__main__":
        main();

