# fir.py
# A class tht implements fir filtering
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch>, 2014
# License: MIT http://opensource.org/licenses/MIT
#

class filtr:
    def __init__(self, nelements=16, defvalue=25):
        self.history = []
        self.f = []
        for i in range(0, nelements):
            self.history.append(defvalue)
            self.f.append(1.0)

    def filt(self, new_value):
        self.history.append(new_value)
        self.history.pop(0)
        i = 0
        fltsum = 0
        fltval = 0
        for val in self.f:
            fltsum = fltsum + self.f[i]
            fltval = fltval + (self.f[i] * self.history[i])
            i = i + 1
        new_value = fltval / fltsum
        return new_value

    def history(self):
        return self.history

    def set_filter(self, new_filt):
        self.f = new_filt
        if len(self.f) > len(self.history):
            for i in range(len(self.history), len(self.f)):
                self.history.append(self.history[i - 1])
        return

