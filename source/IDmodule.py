from datetime import datetime
import math
from uuid import getnode as get_mac


class IDGen:
    """A class for creating IDs
       Usage:
       IDGen_object = IDGen()
       ID = IDGen_object.get_id()"""

    counter = 0    # additional counter
    t_mark = "0"  # time mark used by get_c
    mac = 0  # last 12 bits of mac address

    def __init__(self):
        """ Constructor """
        self.counter = 1
        self.t_mark = self.__epoch()
        self.mac = str(get_mac() & 0x000000000FFF)

    def __get_c(self):
        """ generates extra number for unification.
        should not be called by the user """
        t_mark_2 = self.__epoch()
        if (int(t_mark_2) - int(self.t_mark)) > 1000:  # resets counter if millisecond has passed
            self.t_mark = t_mark_2
            self.counter = 1
        temp = self.__addit_zeros(self.counter)[1:] + str(self.counter)
        self.counter += 1
        return temp

    @staticmethod
    def __addit_zeros(n):
        """ returns x zeros, where x is 4 minus the amount of digits in a number.
         should not be called by the user """
        n_digits = 0
        if n > 0:
            n_digits = int(math.log10(n)) + 1
        elif n == 0:
            n_digits = 1
        return "0" * (4 - n_digits)

    def __epoch(self):
        """returns a string which is a time of a call written without separators.
         should not be called by the user """
        date = datetime.now()
        year = date.year - 2020  # custom epoch
        zeros = self.__addit_zeros(year)
        return """{0}{1}{2}{3}{4}{5}{6}{7}""".format(
                              zeros,
                              str(year),
                              str(date.month),
                              str(date.day),
                              str(date.hour),
                              str(date.minute),
                              str(date.second),
                              str(date.microsecond)
        )

    def get_id(self):
        """returns a new unique ID. should be called by the user"""
        return """1{0}{1}{2}""".format(self.__epoch(), str(self.mac), self.__get_c())


a = IDGen()
print(a.get_id())
