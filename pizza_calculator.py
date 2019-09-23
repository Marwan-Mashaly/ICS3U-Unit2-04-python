#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program calculates the cost of  pizza

import constants


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(input("Enter the diameter of the pizza (inch): "))

    # process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("the cost for a {0} inch pizza  is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
