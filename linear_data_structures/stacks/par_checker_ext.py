# Extend simple paranthesis checker to handle different kinds of opening and closing symbols

from Stack import Stack


def matches(opener, closer):

    openers = "([{"

    closers = ")]}"

    return openers.index(opener) == closers.index(closer)


def par_checker_ext(symbol_string):

    stack = Stack()

    balanced = True

    index = 0

    while index < len(symbol_string) and balanced:

        symbol = symbol_string[index]

        if symbol in "([{":
            stack.push(symbol)
        elif stack.is_empty():
            balanced = False
        else:
            opener = stack.pop()
            closer = symbol
            if not matches(opener, closer):
                balanced = False

        index += 1

    if balanced and stack.is_empty():
        return True

    else:
        return False


