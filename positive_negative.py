#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 05 May 2021
# This program tells if a number is positive, negative or just zero


def main():
    # this function tells if a number is positive, negative or just zero

    # input
    integer = int(input("Enter an integer: "))

    # process & output
    if integer > 0:
        print('{0} is a positive number.'.format(integer))
    elif integer < 0:
        print('{0} is a negative number.'.format(integer))
    else:
        print('{0} is just zero!'.format(integer))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
