#! /usr/bin/python

# A simple Python command line tool to read temperature values
# from an MCP9808 integrated temperature sensor and supply
# them to requests on the network.
#
# Usage: - Start software
#        - Use NetCat to get value: nc ip-address port
#
# This version has exception handling built in.
# by Marco Tedaldi, 19.2.2014
# GNU GPL V3 

import socket # for networking stuff
import smbus  # For i2c stuff
import sys    # for cleanly exit
# import getopt # management of command line option
import time   # for timing stuff (delay)
# import thread # Old threading support
import threading # support for threading


# Use SMBus 1 ("0" in rev. 1 Boards) on the GPIO-Connector
bus = smbus.SMBus(1)

# Port, at which the server will listen for connections
# (Ports below 1024 are only available for root)
port = 7777

# Enter the Address here that you have set on A0-A3
# Don't forget to add 0x18 because of preset bits
address = 0x19 # I2C address of MCP9808


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

def init_net(port):
	try:
		s = socket.socket()
		s.bind(("0.0.0.0",port))
		s.listen(5)
	except:
		sys.stderr.write("\nSomething went wrong while trying to set up Network Socket:\n")
		print "Error:", sys.exc_info()[1]
		sys.exit(7777)
	return s


def handle_connection(conn, r_addr, s_addr):
	try:
		print 'Got a connection from', r_addr 
		temperature = str(get_temperature(s_addr)) + '\n'
		conn.send(temperature)
		conn.close()
	except:
		sys.stderr.write("An unknow error has occured! Terminating...\n")
		print "Error: ", sys.exc_info()[1]



def main():
	sock = init_net(port)
	print "Waiting for connections on port " + str(port)

	while True:
		try:
			c, addr = sock.accept()
			t = threading.Thread(target=handle_connection, args = (c, addr, address) )
			t.daemon = True
			t.start()
			nthreads = threading.activeCount()
			print "Threads open: " + str(nthreads)
		except KeyboardInterrupt:
			sys.stderr.write("\nReceived ctrl+c, will terminate\n")
			sock.shutdown(socket.SHUT_RDWR)
			sock.close()
			sys.exit()
		except:
			sys.stderr.write("An unknow error has occured! Terminating...\n")
			print "Error: ", sys.exc_info()[1]
			sock.close()
			sys.exit(1)


if __name__ == "__main__":
	main();

