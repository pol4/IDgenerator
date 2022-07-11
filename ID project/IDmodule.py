from datetime import datetime
import math
from uuid import getnode as get_mac


class Counter:
    c = 1
    t = "0"
    mac = 0

    def __init__(self):
        self.t = self.epoch()
        self.mac = str(get_mac() & 0x000000000FFF)

    def get_c(self):
        t2 = self.epoch()
        if (int(t2) - int(self.t)) > 1000 or self.c > 100:
            self.t = t2
            self.c = 1
        temp = self.digits(self.c)[1:] + str(self.c)
        self.c += 1
        return temp

    @staticmethod
    def digits(n):
        b = 0
        if n > 0:
            b = int(math.log10(n)) + 1
        elif n == 0:
            b = 1
        return "0" * (4 - b)

    def epoch(self):
        d = datetime.now()
        y = d.year - 2020
        z = self.digits(y)
        return z + str(y)+str(d.month)+str(d.day)+str(d.hour)+str(d.minute)+str(d.second)+str(d.microsecond)

    def get_id(self):
        return int("0" + self.epoch() + str(self.mac) + self.get_c())


a = Counter()
print(a.get_id())
