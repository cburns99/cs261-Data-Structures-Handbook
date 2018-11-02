# the is_empty method simply checks to see if the head of the list is a reference to None. The result of the boolean expression self.head == None will only be true if there are no nodes in the linked list.

def is_empty(self):
    return self.head == None
