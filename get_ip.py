#!/usr/bin/python

import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("130.60.53.30",80))
    ip = str((s.getsockname()[0]))
    s.close
    return ip



