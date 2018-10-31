# Extend the algorithm for binary conversion to perform the conversion for any base

from Stack import Stack


def base_converter(decimal_number, base):

    digits = "0123456789ABCDEF"

    remainder_stack = Stack()

    while decimal_number > 0:

        remainder = decimal_number % base

        remainder_stack.push(remainder)

        decimal_number = decimal_number // base

    new_string = ""

    while not remainder_stack.is_empty():

        new_string += digits[remainder_stack.pop()]

    return new_string
