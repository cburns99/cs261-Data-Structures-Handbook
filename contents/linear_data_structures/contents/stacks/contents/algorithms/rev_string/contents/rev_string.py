
from Stack import Stack


def rev_string(my_str):

    new_str = ""

    stack = Stack()

    for character in my_str:
        stack.push(character)

    for item in range(stack.size()):
        new_str += str(stack.pop())

    return new_str

