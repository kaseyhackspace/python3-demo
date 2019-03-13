#!/usr/bin/env python3
"""
This code says hello world
"""

__author__ = "Hackspace"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    print("1- Celsius to Fahrenheit\n2- Fahrenheit to Celsius\n")
    choice = input('Choose a conversion: ')
    if choice == '1':
        celsius = input('Input celsius:')
        fahrenheit = (float(celsius)*1.8) + 32
        print('celsius:'+celsius)
        print('fahrenheit:'+str(fahrenheit))
    else:
        fahrenheit = input('Input fahrenheit:')
        celsius = (float(fahrenheit)-32) / 1.8
        print('fahrenheit:'+fahrenheit)
        print('celsius:'+str(celsius))
        



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()