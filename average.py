#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program identifies the largest number in a 2D-Array


import random


def calculate(passed_in_2D_list):
    # this function calculatest the average of all the elements in a 2D array
    total = 0
    divider = 0
    total_average = 0

    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
            divider += 1

    total_average = total / divider

    return total_average


def main():
    # this function creates a 2D-Array and prints the average

    random_array = []

    # input
    rows = int(input("How many rows would you like(integer): "))
    columns = int(input("How many columns would you like(integer): "))
    print("")

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            random_number = random.randint(0, 50)
            temp_column.append(random_number)
            print("{0} ".format(random_number), end="")
        random_array.append(temp_column)
        print("")

    average = calculate(random_array)
    print("The average of all these numbers is: {0} ".format(average))


if __name__ == "__main__":
    main()
