#!/usr/bin/python3

# WDT: Watchdog Timer
# A python 3 interface to use the linux watchdog timer
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch> 2014
# License: MIT, http://opensource.org/licenses/MIT

import time # for the delay inside main
import sys # needed for exit
import os # needed for file handling


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
        try:
            self.wdthandle.close()
            ok = True
        except:
            ok = False
        return ok

    def status(self):
        return self.ok





# Main function. Here, mainly as test

def main():
    wd = wdt() # Create watchdog object
    wd.open()  # Open the watchdog file
    print(wd.status()) # print the status (if watchdog could be activated)
    while True:
        try:
            wd.refresh()  # Retrigger the watchdog
            print("Watchdog kicked") # Talk about what you did!
            time.sleep(1.0)  # Wait for one second befor kicking the watchdog again
        except KeyboardInterrupt: # If the user presses ctrl+c
            print("ctrl+c pressed, will terminate")
            wd.deactivate() # Deactivate the watchdog so the system is not rebooted
            wd.finish()     # release the file handle
            sys.exit()       # exit



# Only run main, if this program is called directly (not imported by another program)

if __name__ == "__main__":
        main();


