
<h1>Divide by 2</h1>

<p>The Divide by 2 algorithm takes an argument that is a decimal number and repeatedly divides it by 2. It uses the modulo operator to extract the remainder and then pushes it on the stack. After the division process reaches 0, a binary string is constructed. The binary digits are popped from the stack one at a time and appended to the end of a string. The binary string is then returned.</p>

<h1>Implementation</h1>

```python

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

```

<h1>Example</h1>

[Insert gif here]

<h1>Base Converter</h1>

<p>This algorithm extends the algorithm for binary conversion to perform the conversion for any base</p>

<h1>Implementation</h1>

```python

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

```

<h1>Example</h1>

[Insert gif here]

