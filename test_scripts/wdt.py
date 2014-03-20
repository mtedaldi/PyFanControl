#!/usr/bin/python3

# WDT: Watchdog Timer
# A python 3 interface to use the linux watchdog timer

import time
import os

watchdog = "/dev/watchdog"

def main():
    wdt = open(watchdog, "w")
    while True:
        try:
            wdt.write(" ")
            wdt.flush()
            time.sleep(5)
            print("Watchdog kicked")
        except KeyboardInterrupt:
            print("ctrl+c pressed, will terminate")
            wdt.write("V")
            wdt.flush()
            wdt.close()





if __name__ == "__main__":
        main();


