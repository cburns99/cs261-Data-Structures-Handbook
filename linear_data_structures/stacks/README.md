A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack longest. The most recently added item is the one that is in position to be removed first. This ordering principle is sometimes called LIFO, last-in first-out. It provides an ordering based on length of time in the collection. Stacks are fundamentally important, as they can be used to revers the order of items. The order of insertion is the reverse of the order of removal.

The stack operations are given below.

stack() ~ creates a new stack that is empty. It needs no parameters and returns an empty stack.

push(item) ~ adds a new item to the top of the stack. It needs the item and returns nothing.

pop() ~ removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

peek() ~ returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

isEmpty() ~ tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
