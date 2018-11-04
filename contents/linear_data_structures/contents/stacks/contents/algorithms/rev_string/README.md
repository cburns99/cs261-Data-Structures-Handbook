
<h1>Reverse String</h1>

<p>This algorithm uses a stack to reverse the characteracters in a string.</p>

<h1>Implementation</h1>

```python

from Stack import Stack


def rev_string(my_str):

    new_str = ""

    stack = Stack()

    for character in my_str:
        stack.push(character)

    for item in range(stack.size()):
        new_str += str(stack.pop())

    return new_str

```

<h1>Example</h1>

[Insert gif here]

