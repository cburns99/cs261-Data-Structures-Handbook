
<h1>The Deque Abstract Data Type</h1>

<p>A <strong>deque</strong> (pronounced "deck"), also known as a <strong>double-ended queue</strong>, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. Likewise, existing items can be removed from either end. Even though the deque assumes many of the characteristics of stacks and queues, it does not require the LIFO and FIFO orderings that are enforced by those data structures.</p>

<h1>Operations</h1>

<ul>
  <li><strong>Deque(  )</strong> - creates a new deque that is empty. It needs no parameters and returns an empty deque.

  <li><strong>add_front(item)</strong> - adds a new item to the front of the deque. It needs the item and returns nothing.

  <li><strong>add_rear(item)</strong> - adds a new item to the rear of the deque. It needs the item and returns nothing.

  <li><strong>remove_front(  )</strong> - removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

  <li><strong>remove_rear(  )</strong> - removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

  <li><strong>is_empty(  )</strong> - tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

  <li><strong>size(  )</strong> - returns the number of items in the deque. It needs no parameters and returns an integer.
</ul>

<h1>Implementation</h1>

<p>The details of this deque implementation will be built upon the set of methods used by the Python list. It will assume that the rear of the deque is at position 0 in the list and the front of the deque is at position n-1 in the list.</p>

```python

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

```

<h1>Example</h1>

![](../../../gif/deque.gif)

<h1>Performance</h1>

<p>Big-O efficiency of operations:</p>

[Insert information here]

<h1>Algorithms</h1>

<p>Here is an algorithm that uses a deque:</p>

<ul>
  <li><a href="contents/algorithms/pal_checker">Palindrome Checker</a>
</ul>

