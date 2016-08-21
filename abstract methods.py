from abc import ABCMeta, abstractmethod, abstractproperty


class Movable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def move():
        """Move object"""

    @abstractproperty
    def speed():
        """Object speed"""


class Car(Movable):
    def __init__(self):
        self.speed = 10
        self.x = 0

    def move(self):
        self.c += self.speed

        def speed(self):
            return self.speed


if __name__ == "__main__":
    print(issubclass(Car, Movable))