
from Stack import Stack


def divide_by_2(decimal_number):

    remainder_stack = Stack()

    while decimal_number > 0:
        
        remainder = decimal_number % 2

        remainder_stack.push(remainder)

        decimal_number = decimal_number // 2

    binary_string = ""

    while not remainder_stack.is_empty():

        binary_string += str(remainder_stack.pop())

    return binary_string

