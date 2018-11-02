# The easiest place to add a new node is right at the head, or beginning, of the list. In other
# words, we will make the new item the first item of the list and any existing items will need to
# be linked to this new first item so that they follow. Each item of the list must reside in a node
# object. Line 13 creates a new node and places the item as its data. Now we must complete the
# process by linking the new node into the existing structure. This requires two steps. Step 1
# (line 14) changes the next reference of the new node to refer to the old first node of the list.
# Now that the rest of the list has been properly attached to the new node, we can modify the head
# of the list to refer to the new node. Step 2 (line 15) sets the new node as the head of the list.

from Node import Node

def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp
