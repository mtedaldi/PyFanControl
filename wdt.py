#!/usr/bin/python3

# WDT: Watchdog Timer
# A python 3 interface to use the linux watchdog timer
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch> 2014
# License: MIT, http://opensource.org/licenses/MIT

import time
import os

watchdog = "/dev/watchdog"


# Watchdog timer class

# First, check if the watchdog file exists and is writeable
class wdt:
    def __init__(self, watchdogfile="/dev/watchdog" ):
        self.ok = os.path.exists(watchdogfile)
        if self.ok:
            self.ok = os.access(watchdogfile, os.W_OK)
        return

    # Open the watchdog file for writing.
    # ATTENTION, this already activates the watchdog! If you do not
    # trigger the watchdog within 15 sekonds, the system will reset!
    def open(self):
        if self.ok:
            try:
                self.wdthandle = open(watchdog, "w")
            except:
                self.ok = False
        return self.ok

    # Deactivate the watchdog timer by sending the magic character
    def deactivate(self):
        try:
            self.wdthandle.write("V")
            self.wdthandle.flush()
        except:
            ok = False
        return ok

    # refresh the watchdog
    def refresh(self):
        try:
            self.wdthandle.write(" ")
            self.wdthandle.flush()
            ok = True
        except:
            ok = False
        return ok

    # close (Don't forget the deactivate, before closing!
    def finish(self):
        self.wdthandle.close()
        return

    def status(self):
        print(self.ok)
        return self.ok







def main():
    wd = wdt()
    wd.open()
    wd.status()
    while True:
        try:
            wd.refresh()
            print("Watchdog kicked")
            wd.status()
            time.sleep(1.0)
        except KeyboardInterrupt:
            print("ctrl+c pressed, will terminate")
            wd.deactivate()
            wd.finish()
            os.exit()





if __name__ == "__main__":
        main();


