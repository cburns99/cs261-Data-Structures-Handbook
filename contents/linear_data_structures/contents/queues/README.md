
<h1>The Queue Abstract Data Type</h1>

<p>A <strong>queue</strong> is an ordered collection of items where the addition of new items happens at one end, commonly called the "rear", and the removal of existing items occurs at the other end, commonly called the "front". As an element enters the queue, it starts at the rear and makes its way toward the front, waiting until it is the next element to be removed. The most recently added item in the queue must wait at the end of the collection. The item that has been in the collection the longest is at the front. This ordering principle is sometimes called <strong>FIFO</strong>, first-in first-out.</p>

<h1>Operations</h1>

<ul>
  <li><strong>Queue(  )</strong> - creates a new queue that is empty. It needs no parameters and returns an empty queue.

  <li><strong>enqueue(item)</strong> - adds a new item to the rear of the queue. It needs the item and returns nothing.

  <li><strong>dequeue(  )</strong> - removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.

  <li><strong>is_empty(  )</strong> - tests to see whether the queue is empty. It needs no parameters and returns a boolean value.

  <li><strong>size(  )</strong> - returns the number of items in the queue. It needs no parameters and returns an integer.
</ul>

<h1>Implementation</h1>

<p>As before, we will use the power and simplicity of the Python list collection to build the internal representation of the queue. This implementation assumes that the rear is at position 0 in the list. This allows us to use the <strong>insert</strong> function on lists to add new elements to the rear of the queue. The <strong>pop</strong> operation can be used to remove the front element (the last element of the list).</p>

```python

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

```

<h1>Example</h1>

![](../../../gif/queue.gif)

<h1>Performance</h1>

<p>Big-O efficiency of operations:</p>

[Insert information here]

<h1>Algorithms</h1>

<p>Here are a few algorithms that use queues:</p>

<ul>
  <li><a href="contents/algorithms/...">[Insert algorithm here]</a>
</ul>

