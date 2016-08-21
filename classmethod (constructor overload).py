# coding:utf-8
"""
@classmethod - method which can be used from class, not from instants.
First arg of method with this decorator is class, not object
So we can OVERLOAD CONSTRUCTOR

@classmethod - метод, который есть у класс, вне зависимости от объекта.
Первым аргументом передается класс, а не объект


"""
import datetime


class Date(object):
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{} {} {}".format(self.day, self.month, self.year)

    @classmethod
    def now(cls):
        now = datetime.datetime.now()
        return cls(now.day, now.month, now.year)

    @classmethod
    def first_date_in_year(cls, year):
        return cls(1, 1, year)


if __name__ == '__main__':
    # Usual way to create object
    d = Date(2, 10, 1996)
    print(d)

    # Using another constructor
    d = Date.now()
    print(d)

    # Another constructor with argunents
    d = Date.first_date_in_year(2016)
    print(d)
