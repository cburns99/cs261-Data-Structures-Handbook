# The unordered list will be built from a collection of nodes, each link to the next by explicit
# references. As long as we know where to find the first node (containing the first item), each item
# after that can be found by successively following the next links. With this in mind, the UnorderedList
# class must maintain a reference to the first node. It is very important to note that the list class
# itself does not contain any node objects. Instead it contains a single reference to only the first node
# in the linked structure. The easiest place to add a new node is right at the head, or beginning, of the
# list. In other words, we will make the new item the first item of the list and the existing items will
# need to be linked to this new first item so that they follow.

from Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
    
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


