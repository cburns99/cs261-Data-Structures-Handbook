# This algorithm takes a string of characters as input and checks whether or not it is a palindrome.
# It processes the string from left to right and adds each character to the rear of the deque. The
# front of the deque will hold the first character of the string and the rear of the deque will hold
# the last character. It removes both first and last items directly, compares them, and if they match,
# continues until there are no more items left or one item left depending on whether the length of the
# original string was even or odd.

from Deque import Deque

def pal_checker(string):
    
    character_deque = Deque()

    for character in string:

        character_deque.add_rear(character)

    still_equal = True

    while character_deque.size() > 1 and still_equal:

        first_character = character_deque.remove_front()

        last_character = character_deque.remove_rear()

        if first_character != last_character:

            still_equal = False

    return still_equal
