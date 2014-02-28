#!/usr/bin/python

# This is just a test program to learn, how variables in Python work


def change_value(val):
    val[0] = val[0] + 3
    print str(val) + "\n"
    return

def main():
    a = [0]
    a[0] = 5
    print str(a) + "\n"
    change_value(a)
    print str(a) + "\n"

main()
