# Write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced. To solve this problem we need to make an important observation. Closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out. This is a clue that stacks can be used to solve the problem. Starting with an empty stack, process the paranthesis strings from left to right. If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. If, on the other hand, a symbol is a closing paranthesis, pop the stack. As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly. At the end of the string, when all symbols have been processed, the stack should be empty.

from Stack import Stack

def parChecker(symbol_string):

    s = Stack()

    balanced = True

    index = 0

    while index < len(symbol_string) and balanced:

        symbol = symbol_string[index]

        if symbol == "(":
            s.push(symbol)
        elif s.isEmpty():
            balanced = False
        else:
            s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
