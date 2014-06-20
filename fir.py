# fir.py
# A class that implements fir filtering
#
# (c) Marco Tedaldi <tedaldi@hifo.uzh.ch>, 2014
# License: MIT http://opensource.org/licenses/MIT
#

class filtr:
    # The init method is called on creation of the object
    def __init__(self, nelements=16, defvalue=25):
        self.history = []
        self.f = []
        for i in range(0, nelements):
            self.history.append(defvalue) # build a default filter (sliding window)
            self.f.append(1.0/nelements) #make sure, that the sum of the filter is 1)

    # adds a new value to the list and returns the updated filtered value
    def filt(self, new_value):
        self.history.append(new_value) # append the new input to the end of the list
        self.history.pop(0) # remove the oldest value
        i = 0
        fltsum = 0
        fltval = 0
        for val in self.f:
            fltval = fltval + (self.f[i] * self.history[i]) # multiply+add every element with the filter
            i = i + 1
        new_value = fltval
        return new_value

    # returns the history values used for the filter
    def history(self):
        return self.history

    # replaces the filter parameters with new ones
    def set_filter(self, new_filt):
        s = sum(new_filt) # sum all the elements of the new filter to make sure the sum is one
        new_filt[:] = [c/s for c in new_filt] # divide every element by the offset to 1
        self.f = new_filt
        if len(self.f) > len(self.history):
            for i in range(len(self.history), len(self.f)):
                self.history.append(self.history[i - 1])
        return


def main():
    return

if __name__ == "__main__":
    main();

