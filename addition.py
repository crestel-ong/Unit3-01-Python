#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is the addition program
#  user inputs the numbers to be added


def main():
    # this function calculate the sum to two integers

    # input
    first_number = int(input("Enter the first number (integer) to add: "))
    second_number = int(input("Enter the second number (integer) to add: "))

    # process
    sum = first_number + second_number

    # output
    print("{0} + {1} = {2}".format(first_number, second_number, sum))
    print("\nDone.")


if __name__ == "__main__":
    main()
