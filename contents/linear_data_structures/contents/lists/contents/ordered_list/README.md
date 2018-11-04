
<h1>The Ordered List Abstract Data Type</h1>

<p>The structure of an <strong>ordered list</strong> is a collection of items where each item holds a relative position that is based upon some underlying characteristic of the item. The ordering is typically either ascending or descending and we assume that list items have a meaningful comparison operation that is already defined.</p>

<h1>Operations</h1>

<ul>
  <li><strong>OrderedList(  )</strong> - creates a new ordered list that is empty. It needs no parameters and returns an empty list.

  <li><strong>add(item)</strong> - adds a new item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.

  <li><strong>remove(item)</strong> - removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.

  <li><strong>search(item)</strong> - searches for the item in the list. It needs the item and returns a boolean value.

  <li><strong>is_empty(  )</strong> - tests to see whether the list is empty. It needs no parameters and returns a boolean value.

  <li><strong>length(  )</strong> - returns the number of items in the list. It needs no parameters and returns an integer.

  <li><strong>index(item)</strong> - returns the position of the item in the list. It needs the item and returns the index. Assume the item is in the list.

  <li><strong>pop(  )</strong> - removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

  <li><strong>pop(pos)</strong> - removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
</ul>

<h1>Implementation</h1>

<p>Again, the node and link structure is ideal for representing the relative position of the items in an unordered list. It is given again here for reference.</p>

```python

class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

```

<h1>The Head of the List</h1>

<p>To implement the <strong>OrderedList</strong> class, we will use the same technique as seen previously with unordered lists. Once again, an empty list will be denoted by a <strong>head</strong> reference to <strong>None</strong>.</p>

```python

class OrderedList:

    def __init__(self):
        self.head = None

```

<h1>The is_empty, length, and add Methods</h1>

<p>As we consider the operations for the ordered list, we should note that the <strong>is_empty</strong> and <strong>length</strong> methods can be implemented the same as with unordered lists since they deal only with the number of nodes in the list without regard to the actual item values. Likewise, the <strong>remove</strong> method will work just fine since we still need to find the item and then link around the node to remove it. These methods are given again here for reference.

```python

    def is_empty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

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

```

<h1>The search Method</h1>

<p>The search of an unordered linked list required that we traverse the nodes one at a time until we either find the item we are looking for or run out of nodes (None). In the case where we find the item, this approach is exactly what we need. However, in the case where the item is not in the list, we can take advantage of the ordering to stop the search early. Once the value in the node becomes greater than the item we are searching for, the search can stop and return False. There is no way the item could exist further out in the linked list. It is easy to incorporate this new condition by adding another boolean variable, <strong>stop</strong>, and initializing it to <strong>False</strong> (line 42). While stop is False we can continue to look forward in the list (line 43). If a node is discovered that contains data greater than the item we are looking for, we will set stop to <strong>True</strong> (lines 46-47). The remaining lines are identical to the unordered list search.</p>

```python

38| 
39|     def search(self, item):
40|         current = self.head
41|         found = False
42|         stop = False
43|         while current != None and not found and not stop:
44|             if current.get_data() == item:
45|                 found = True
46|             elif current.getData() > item:
47|                 stop = True
48|             else:
49|                 current = current.get_next()
50|         return found
51| 

```

<h1>The add Method</h1>

<p>The most significant method modification will take place in <strong>add</strong>. Recall that for unordered lists, the add method could simply place a new node at the head of the list. It was the easiest point of access. This will no longer work with ordered lists. It is now necessary that we discover the specific place where a new item belongs in the existing ordered list. We need to traverse the linked list looking for the place where the new node will be added. We'll know we have found that place when either we run out of nodes (current becomes None) or the value of the current node becomes greater than the item we wish to add. As we saw with unordered lists, it is necessary to have an additional reference, again called <strong>previous</strong>, since current will not provide access to the node that must be modified. Lines 14-15 set up the two external references and lines 21-22 again allow previous to follow one node behind current every time through the iteration. The condition (line 17) allows the iteration to continue as long as there are more nodes and the value in the current node is not larger than the item. In either case, when the iteration fails, we have not found the location for the new node. Once a new node has been created for the item, the only remaining question is whether the new node will be added at the beginning of the linked list or some place in the middle. Again, <strong>previous == None</strong> (line 24) can be used to provide the answer.</p>

```python

12| 
13|     def add(self, item):
14|         current = self.head
15|         previous = None
16|         stop = False
17|         while current != None and not stop:
18|             if current.get_data() > item:
19|                 stop = True
20|             else:
21|                 previous = current
22|                 current = current.getNext()
23|         temp = Node(item)
24|         if previous == None:
25|             temp.set_next(self.head)
26|             self.head = temp
27|         else:
28|             temp.set_next(current)
29|             previous.set_next(temp)
30| 

```

<h1>Putting It All Together</h1>

<p>Below is the full <strong>OrderedList</strong> class definition.</p>

```python

from Node import Node


class OrderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.get_next()
        return found

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

```

<h1>Example</h1>

![](../../../gif/[placeholder].gif)

<h1>Performance</h1>

<p>Big-O efficiency of operations:</p>

[Insert information here]

<p></p>

<h1>Algorithms</h1>

<p>Here are a few algorithms that use [placeholder]:</p>

<ul>
  <li><a href="contents/algorithms/...">[placeholder]</a>
</ul>

