# coding:utf-8
"""
@staticmethod - method which exists for any instance of class

"""
import datetime


class Date():
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{} {} {}".format(self.day, self.month, self.year)

    @staticmethod
    def in_computer_era(year):
        return year >= 1970


if __name__ == '__main__':
    # Using static method
    print(Date.in_computer_era(2000))
