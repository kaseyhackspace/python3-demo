#!/usr/bin/env python3
"""
This code says hello world
"""

__author__ = "Hackspace"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    print("hello world")
    celsius = input('Input celsius here: ')
    farenheit = (float(celsius)*1.8) + 32
    print('celsius:'+celsius)
    print('farenheit:'+str(farenheit))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()