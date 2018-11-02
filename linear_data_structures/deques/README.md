# The Deque Abstract Data Type

A deque (pronounced "deck"), also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear (giggity), and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear (giggity). Likewise, existing items can be removed from either end. Even though the deque assumes many of the characteristics of stacks and queues, it does not require the LIFO and FIFO orderings that are enforced by those data structures.

The deque operations are given below.

Deque() ~ creates a new deque that is empty. It needs no parameters and returns an empty deque.

add_front(item) ~ adds a new item to the front of the deque. It needs the item and returns nothing.

add_rear(item) ~ adds a new item to the rear of the deque. It needs the item and returns nothing.

remove_front() ~ removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

remove_rear() ~ removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

is_empty() ~ tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

size() ~ returns the number of items in the deque. It needs no parameters and returns an integer.
