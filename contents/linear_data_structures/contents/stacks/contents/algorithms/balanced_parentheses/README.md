
<h1>Balanced Parentheses</h1>

<p>This algorithm reads a string of parentheses from left to right and decides whether the symbols are balanced. It's important to observe that closing symbols will match opening symbols in the reverse order of their appearance; they match from the inside out. This is a clue that stacks can be used to solve the problem. Starting with an empty stack, we process the parenthesis strings from left to right. If a symbol is an opening parenthesis, we push it on the stack as a signal that a corresponding closing symbol needs to appear later. If, on the other hand, a symbol is a closing parenthesis, we pop the stack. As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. At the end of the string, when all symbols have been processed, the stack will be empty and our function will return True. If at any time there is no opening symbol on the stack to match a closing symbol, our function will return False and we will be able determine that the string is not balanced properly.</p>

<h1>Implementation</h1>

```python

from Stack import Stack


def par_checker(symbol_string):

    stack = Stack()

    balanced = True

    index = 0

    while index < len(symbol_string) and balanced:

        symbol = symbol_string[index]

        if symbol == "(":
            stack.push(symbol)
        elif stack.is_empty():
            balanced = False
        else:
            stack.pop()

        index += 1

    if balanced and stack.is_empty():
        return True

    else:
        return False

```

<h1>Example</h1>

[Insert gif here]

<h1>Balanced Symbols</h1>

<p>This algorithm extends the simple parenthesis checker to handle different kinds of opening and closing symbols.</p>

<h1>Implementation</h1>

```python

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

```

<h1>Example</h1>

[Insert gif here]

