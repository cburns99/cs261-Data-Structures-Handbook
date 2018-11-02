# The details of this deque implementation will be built upon the set of methods used by the Python list. It will assume that the rear of the deque is at position 0 in the list and the front of the deque is at position n-1 in the list.


class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


