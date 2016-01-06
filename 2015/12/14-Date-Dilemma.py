# Problem: 245 [Easy] Date Dilemma
# https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/
# Author: ExcaliburZero
# License: MIT

import fileinput


def is_int(character):
    """
    A function which returns whether or not a given character is an integer.

    :param str character: The character to check.
    :returns bool: Whether or not the given character is an integer.
    """
    try:
        int(character)
        return True
    except ValueError:
        return False


def get_values(date):
    """
    A function which breaks up a given date into the various numerical values
    that comprise it.

    :param str date: The date to get the values of.
    :returns list: The values contained in the given date, as integers.
    """
    values = []
    digits = ""
    # Iterate over each of the characters in the date
    for character in date:
        # If the character is an integer then record it
        if is_int(character):
            digits += character
        # If the character is a non-integer, then record the previous digits as
        # a number, and empty the digit buffer
        else:
            values.append(int(digits))
            digits = ""
    # Get the last number if it exists
    if len(digits) > 0:
        values.append(int(digits))
    return values


def is_ymd(date):
    """
    A function which returns whether a date is in ymd format or not.

    :param list date: The date to check the format of, as a list of its numbers
    in the order they are given.
    :returns bool: Whether the given date is in ymd format or not.
    """
    # Check whether or not the first number is a year
    if date[0] > 999:
        return True
    else:
        return False


def num_to_2_char(number):
    """
    A function which takes in a number and pads it to 2 charcters and returns
    it as a string.

    :param int number: The number as an integer.
    :returns str: The number padded to two digits as a string.
    """
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


def get_date(date):
    """
    A function which returns the ISO 8601 version of the supplied date.

    :param str date: The date in an uncertain format.
    :returns str: The given date in the ISO8601 specified format.
    """
    # Convert the date to its values
    values = get_values(date)

    # Check what format the date is in, and return it in the ISO 8601 form
    if is_ymd(get_values(date)):
        return str(values[0]) + "-" + num_to_2_char(values[1]) + "-" + \
            num_to_2_char(values[2])
    else:
        # Handle if the year is given without the first two digits
        if values[2] < 1000:
            values[2] += 2000
        return str(values[2]) + "-" + num_to_2_char(values[0]) + "-" + \
            num_to_2_char(values[1])


def main():
    """
    A function which prints out the dates given in standard input in the ISO
    8601 format.
    """
    # Iterate over the lines in standard input
    for line in fileinput.input():
        # Print out each of the dates in ISO 8601
        print(get_date(line[:-1]))


# Run the main function of the script
if __name__ == '__main__':
    main()
