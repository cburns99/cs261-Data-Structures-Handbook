
<h1>The Unordered List Abstract Data Type</h1>

<p>An <strong>unordered list</strong> is a collection of items where each item holds a relative position with respect to the others. We can consider the list as having a first item, a second item, a third item, and so on. We can also refer to the beginning of the list (the first item) or the end of the list (the last item). For simplicity, we will assume that lists cannot contain duplicate items.</p>

<h1>Operations</h1>

<ul>
  <li><strong>List(  )</strong> - creates a new list that is empty. It needs no parameters and returns an empty list.

  <li><strong>add(item)</strong> - adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.

  <li><strong>remove(item)</strong> - removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.

  <li><strong>search(item)</strong> - searches for the item in the list. It needs the item and returns a boolean value.

  <li><strong>is_empty(  )</strong> - tests to see whether the list is empty. It needs no parameters and returns a boolean value.

  <li><strong>length(  )</strong> - returns the number of items in the list. It needs no parameters and returns an integer.

  <li><strong>append(item)</strong> - adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.

  <li><strong>index(item)</strong> - returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.

  <li><strong>insert(pos, item)</strong> - adds a new item to the list at position pos. It need the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.

  <li><strong>pop(  )</strong> - removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

  <li><strong>pop(pos)</strong> - removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
</ul>

<h1>Implementation</h1>

<p>In order to implement an unordered list, we will construct what is commonly known as a <strong>linked list</strong>. We need to be sure that we can maintain the relative positioning of the items. However, there is no requirement that we maintain that positioning in contiguous memory. If we can maintain some explicit information in each item, namely the location of the next item, then the relative position of each item can be expressed by simply following the link from one item to the next. It is important to note that the location of the first item of the list must be explicitly specified. Once we know where the first item is, the first item can tell us where the second is, and so on. The external reference is often referred to as the <strong>head</strong> of the list. Similarly, the last item needs to know that there is no next item.</p>

<h3>Node Class</h3>

<p>The basic building block for the linked list implementation is the <strong>node</strong>. Each node object must hold at least two pieces of information. First, the node must contain the list item itself. We will call this the <strong>data field</strong> of the node. In addition, each node must hold a reference to the next node. The special Python reference value <strong>None</strong> will play an important role in the Node class and later in the linked list itself. A reference to None will denote the fact that there is no next node.</p>

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

<h3>The Head of the List</h3>

<p>The special reference None will be used to state that the head of the list does not refer to anything. Eventually, the head of the list will refer to the first node which will contain the first item of the list. In turn that node will hold a reference to the next node (the next item) and so on. It is very important to note that the list class itself will not contain any node objects. Instead, it will contain a single reference to only the first node in the linked structure.</p>

```python

class UnorderedList:

    def __init__(self):
        self.head = None

```
<h3>The is_empty Method</h3>

<p>the <strong>is_empty</strong> method simply checks to see if the head of the list is a reference to None. The result of the boolean expression <strong>self.head == None</strong> will only be true if there are no nodes in the linked list.</p>

```python

def is_empty(self):
    return self.head == None

```

<h3>The add Method</h3>

<p>The easiest place to add a new node is right at the head, or beginning, of the list. In other words, we will make the new item the first item of the list and any existing items will need to be linked to this new first item so that they follow. Each item of the list must reside in a node object. Line 10 creates a new node and places the item as its data. Now we must complete the process by linking the new node into the existing structure. This requires two steps. Step 1 (line 11) changes the next reference of the new node to refer to the old first node of the list. Now that the rest of the list has been properly attached to the new node, we can modify the head of the list to refer to the new node. Step 2 (line 12) sets the new node as the head of the list.</p>

```python

 8| 
 9|     def add(self, item):
10|         temp = Node(item)
11|         temp.set_next(self.head)
12|         self.head = temp
13| 

```

<h3>The length Method</h3>

<p>To implement the <strong>length</strong> method, we need to use a technique known as <strong>linked list traversal</strong>. Traversal refers to the process of systematically visiting each node. To do this we use an external reference that starts at the first node in the list. As we visit each node, we move the reference to the next node by "traversing" the next reference. We need to traverse the linked list and keep a count of the number of nodes that occurred. The external reference is called <strong>current</strong> and is initialized to the head of the list in line 15. At the start of the process we have not seen any nodes so the count is set to 0. Lines 17-19 implement the traversal. As long as the current reference has not seen the end of the list (None), we move current along to the next node via the assignment statement in line 19. Every time current moves to a new node, we add 1 to count (line 18). Finally, count gets returned after the iteration stops (line 20).</p>

```python

13| 
14|     def length(self):
15|         current = self.head
16|         count = 0
17|         while current != None:
18|             count += 1
19|             current = current.get_next()
20|         return count
21| 

```

<h3>The search Method</h3>

<p>Searching for a value in a linked list implementation of an unordered list also uses the traversal technique. As we visit each node in the linked list we will ask whether the data stored there matches the item we are looking for. In this case, however, we may not have to traverse all the way to the end of the list. In fact, if we do get to the end of the list, that means that the item we are looking for must not be present. Also, if we do find the item, there is no need to continue. The traversal is initialized to start at the head of the list (line 23). We use a boolean variable called <strong>found</strong> to remember whether we have located the item we are searching for. Since we have not found the item at the start of the traversal, found can be set to False (line 24). The iteration in line 25 takes into account both conditions discussed above. As long as there are more nodes to visit and we have not found the item we are looking for, we continue to check the next node. The question in line 26 asks whether the data item is present in the current node. If so, found can be set to True.</p>

```python

21| 
22|     def search(self, item):
23|         current = self.head
24|         found = False
25|         while current != None and not found:
26|             if current.get_data() == item:
27|                 found = True
28|             else:
29|                 current = current.get_next()
30|         return found
31| 

```

<h3>The remove Method</h3>

<p>The <strong>remove</strong> method requires two logical steps. First, we need to traverse the list looking for the item we want to remove. Once we find the item, we must remove it. Starting with an external reference set to the head of the list, we traverse the links until we discover the item we are looking for. Since we assume that the item is present, we know that the iteration will stop before current gets to None. This means that we can simply use the boolean found in the condition. In order to remove the node containing the item, we must use two external references as we traverse down the linked list. current will mark the current location of the traverse. The new reference, which we will call <strong>previous</strong>, will always travel one node behind current. That way, when current stops at the node to be removed, previous will be referring to the proper place in the linked list for modification. Lines 33-34 assign initial values to the two references. Note that current starts out at the list head. previous, however, is assumed to always travel one node behind current. For this reason, previous starts out with a value of None since there is no node before the head. The boolean variable found will be used to control the iteration. In lines 37-38 we ask whether the item stored in the current node is the item we wish to remove. If so, found can be set to True. If we do not find the item, previous and current must both be moved one node ahead. The order of these two statements is crucial. previous must first be moved one node ahead to the location of current. At that point, current can be moved. This process is often referred to as "inch-worming". Once the searching step of the remove has been completed we need to remove the node from the linked list. However, there is a special case that needs to be addressed. If the item to be removed happens to be the first item in the list, then current will reference the first node in the linked list. This also means that previous will be None. previous refers to the node whose next reference needs to be modified in order to complete the remove. In this case, it is not previous but rather the head of the list that needs to be changed. Line 43 allows us to check whether we are dealing with this special case. If previous did not move, it will still have the value None when the boolean found becomes True. In that case (line 44) the head of the list is modified to refer to the node after the current node, in effect removing the first node from the linked list. However, if previous is not None, the node to be removed is somewhere down the linked list structure. In this case the previous reference is providing us with the node whose next reference must be changed. Line 46 uses the <strong>set_next</strong> method from previous to accomplish the removal.</p>

```python

31| 
32|     def remove(self, item):
33|         current = self.head
34|         previous = None
35|         found = False
36|         while not found:
37|             if current.get_data() == item:
38|                 found = True
39|             else:
40|                 previous = current
41|                 current = current.get_next()
42|     
43|         if previous == None:
44|             self.head = current.get_next()
45|         else:
46|             previous.set_next(current.get_next())
47|

```

<h3>Putting It All Together</h3>

<p>Below is the full <strong>UnorderedList</strong> class definition.</p>

```python

from Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

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
        while current != None and not found:
            if current.get_data() == item:
                found = True
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

![](../../../../../gif/[placeholder].gif)

<h1>Performance</h1>

<p>Big-O efficiency of operations:</p>

[Insert information here]

<p></p>

