"""
Design by contract sample.

Git: https://github.com/deadpixi/contracts

"""
from dpcontracts import *


@invariant("X and Y must be positive", lambda: self.x >= 0 and self.y >= 0)
class Calculate:
    @require("X  must be integers", lambda: isinstance(x, int))
    @require("Y  must be integers", lambda: isinstance(y, int))
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @ensure("Wrong work", lambda: __result__ == self.x + self.y)
    def add(self):
        return self.x + self.y



c = Calculate(1, 1)
c.add()
c.inc_x()
