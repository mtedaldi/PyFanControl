# fir.py
# A class that implements iir filtering
# The IIR filter is implemented as direct-form 2 transposed.
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch>, 2014
# License: MIT http://opensource.org/licenses/MIT
#

class iis:
    # The init method is called on creation of the object
    def __init__(self, nelements=16, defvalue=25):
        self.history = []
        self.f = []
        for i in range(0, nelements):
            self.history.append(defvalue)
            self.f.append(1.0/nelements)

    # adds a new value to the list and returns the updated filtered value
    def filt(self, new_value):
        self.history.append(new_value)
        self.history.pop(0)
        i = 0
        fltsum = 0
        fltval = 0
        for val in self.f:
#            fltsum = fltsum + self.f[i]
            fltval = fltval + (self.f[i] * self.history[i])
            i = i + 1
#        new_value = fltval / fltsum
        new_value = fltval
        return new_value

    # returns the history values used for the filter
    def history(self):
        return self.history

    # replaces the filter parameters with new ones
    def set_filter(self, new_filt_a, new_filt_b):
        self.a = new_filt_a
        self.b = new_filt_b
        if len(self.f) > len(self.history):
            for i in range(len(self.history), len(self.f)):
                self.history.append(self.history[i - 1])
        return


