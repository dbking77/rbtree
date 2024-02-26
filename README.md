# About

Basic red/black tree implementation based on this [description](https://www.youtube.com/watch?v=aPqz3jyl8ak)

# Usage
Red/black tree only stores keys not any values.  There is an insert function, but no remove function.

**Tree** 
- insert : inserts a node with an integer key value
- validate : validates tree connectivity, ordering, and red/black tree invarients:
  - child node's parent is parent
  - left node key is less than parent, and right node key is greater than parent
  - root node black
  - no adjacent red nodes occur on any path to a terminal node
  - all count of black nodes on any path to terminal nodes are equal for entire tree
- print : prints tree side-ways on the terminal.  Right side of tree is on top, left side faces downward.

## Test
There is a set of pytest unit tests to validate RB-tree insert and invariants.
```
pytest
```