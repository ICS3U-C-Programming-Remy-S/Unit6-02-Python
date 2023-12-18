#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Dec 17, 2023
# This program will find the max of
# 10 numbers

import random
import constants


def find_max_value(list_of_int):
    # Initialize counter
    counter = 0

    # Initialize max_value to cell 0 in the list
    max_value = list_of_int[0]

    # Loop through the list to find the maximum value
    while counter < constants.MAX_ARRAY_SIZE:
        # increment
        counter += counter

        # find max
        if list_of_int[counter] > max_value:
            max_value = list_of_int[counter]
    return max_value


def main():
    # create list
    list_of_int = []

    # for loop to populate list
    for counter in range(constants.MAX_ARRAY_SIZE):
        list_of_int[counter] = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # display added numbers
        print(f"{list_of_int[counter]} added to list")

    # call find_max_value function
    max_value = find_max_value(list_of_int)

    # display max value
    print("Max Value is:", max_value)


if __name__ == "__main__":
    main()
