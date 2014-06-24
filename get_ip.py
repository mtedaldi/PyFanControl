#!/usr/bin/python
# A simple function to get the IP address of the
# host. You have to use a reachable IP-Address!
# This is to prevent getting 127.0.0.1 as result
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch>, 2014
# License: MIT, http://opensource.org/licenses/MIT

import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("130.60.53.30",80))
    ip = str((s.getsockname()[0]))
    s.close
    return ip


if __name__ == "__main__":
        print(get_ip())

