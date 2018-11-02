# To implement the length method, we need to use a technique known as linked list traversal. Traversal refers to the process of systematically visiting each node. To do this we use an external reference that starts at the first node in the list. As we visit each node, we move the reference to the next node by "traversing" the next reference. We need to traverse the linked list and keep a count of the number of nodes that occurred. The external reference is called current and is initialized to the head of the list in line 4. At the start of the process we have not seen any nodes so the count is set to 0. Lines 6-8 implement the traversal. As long as the current reference has not seen the end of the list (None), we move current along to the next node via the assignment statement in line 8. Every time current moves to a new node, we add 1 to count (line 7). Finally, count gets returned after the iteration stops (line 9).

def length(self):
    current = self.head
    count = 0
    while current != None:
        count += 1
        current = current.get_next()
    return count

