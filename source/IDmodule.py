from datetime import datetime
import math
from uuid import getnode as get_mac


class IDGen:
    """A class for creating IDs
       Usage:
       counter_object = Counter()
       ID = counter_object.get_id()"""

    c = 0    # additional counter
    t = "0"  # time mark used by get_c
    mac = 0  # last 12 bits of mac address

    def __init__(self):
        """ Constructor """
        self.c = 1
        self.t = self.epoch()
        self.mac = str(get_mac() & 0x000000000FFF)

    def get_c(self):
        """ generates extra number for unification.
        should not be called by the user """
        t2 = self.epoch()
        if (int(t2) - int(self.t)) > 1000 or self.c > 100:  # resets counter if millisecond has passed or c > 100
            self.t = t2
            self.c = 1
        temp = self.digits(self.c)[1:] + str(self.c)
        self.c += 1
        return temp

    @staticmethod
    def digits(n):
        """ returns x zeros, where x is 4 minus the amount of digits in a number.
         should not be called by the user """
        b = 0
        if n > 0:
            b = int(math.log10(n)) + 1
        elif n == 0:
            b = 1
        return "0" * (4 - b)

    def epoch(self):
        """returns a string which is a time of a call written without separators.
         should not be called by the user """
        d = datetime.now()
        y = d.year - 2020  # custom epoch
        z = self.digits(y)
        return z + str(y)+str(d.month)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)+str(d.microsecond)

    def get_id(self):
        """returns a new unique ID. should be called by the user"""
        return int("0" + self.epoch() + str(self.mac) + self.get_c())

