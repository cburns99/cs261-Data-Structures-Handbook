# The special reference None will be used to state that the head of the list does not refer to
# anything. Eventually, the head of the list will refer to the first node which will contain the
# first item of the list. In turn that node will hold a reference to the next node (the next item)
# and so on. It is very important to note that the list class itself will not contain any node
# objects. Instead, it will contain a single reference to only the first node in the linked
# structure.

class UnorderedList:

    def __init__(self):
        self.head = None

