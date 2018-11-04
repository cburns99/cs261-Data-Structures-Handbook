
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

