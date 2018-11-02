# Searching for a value in a linked list implementation of an unordered list also uses the
# traversal technique. As we visit each node in the linked list we will ask whether the data
# stored there matches the item we are looking for. In this case, however, we may not have to
# traverse all the way to the end of the list. In fact, if we do get to the end of the list,
# that means that the item we are looking for must not be present. Also, if we do find the
# item, there is no need to continue. The traversal is initialized to start at the head of
# the list (line 16). We use a boolean variable called found to remember whether we have
# located the item we are searching for. Since we have not found the item at the start of
# the traversal, found can be set to False (line 17). The iteration in line 18 takes into
# account both conditions discussed above. As long as there are more nodes to visit and we
# have not found the item we are looking for, we continue to check the next node. The
# question in line 19 asks whether the data item is present in the current node. If so,
# found can be set to True.

def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
        if current.get_data() == item:
            found = true
        else:
            current = current.get_next()
    return found

