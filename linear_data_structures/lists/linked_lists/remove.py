# The remove method requires two logical steps. First, we need to traverse the list looking for the
# item we want to remove. Once we find the item, we must remove it. Starting with an external
# reference set to the head of the list, we traverse the links until we discover the item we are
# looking for. Since we assume that the item is present, we know that the iteration will stop before
# current gets to None. This means that we can simply use the boolean found in the condition. In
# order to remove the node containing the item, we must use two external references as we traverse
# down the linked list. Current will mark the current location of the traverse. The new reference,
# which we will call previous, will always travel one node behind current. That way, when current
# stops at the node to be removed, previous will be referring to the proper place in the linked
# list for modification. Lines 33-34 assign initial values to the two references. Note that current
# starts out at the list head. previous, however, is assumed to always travel one node behind
# current. For this reason, previous starts out with a value of None since there is no node before
# the head. The boolean variable found will be used to control the iteration. In lines 37-38 we
# ask whether the item stored in the current node is the item we wish to remove. If so, found
# can be set to True. If we do not find the item, previous and current must both be moved one
# node ahead. The order of these two statements is crucial. previous must first be moved one
# node ahead to the location of current. At that point, current can be moved. This process is
# often referred to as "inch-worming". Once the searching step of the remove has been completed
# we need to remove the node from the linked list. However, there is a special case that needs
# to be addressed. If the item to be removed happens to be the first item in the list, then
# current will reference the first node in the linked list. This also means that previous will
# be None. previous refers to the node whose next reference needs to be modified in order to
# complete the remove. In this case, it is not previous but rather the head of the list that
# needs to be changed. Line 43 allows us to check whether we are dealing with the special case
# described above. If previous did not move, it will still have the value None when the boolean
# found becomes True. In that case (line 44) the head of the list is modified to refer to the
# node after the current node, in effect removing the first node from the linked list. However,
# if previous is not None, the node to be removed is somewhere down the linked list structure.
# In this case the previous reference is providing us with the node whose next reference must
# be changed. Line 46 uses the set_next method from previous to accomplish the removal.

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

