
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

<p>To implement the <strong>OrderedList</strong> class, we will use the same technique as seen previously with unordered lists. Once again, an empty list will be denoted by a <strong>head</strong> reference to <strong>None</strong>.</p>

```python


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

