#!/usr/bin/env python

# MIT License

# Copyright (c) 2024 Derek King

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

from typing import List, Optional


class Node:
    """
    Node for Red/Black tree structure
    """

    def __init__(self, key: int, *,
                 parent: Optional['Node'] = None,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None,
                 red: bool = True):
        self.parent: Optional['Node'] = parent
        self.right: Optional['Node'] = right
        if right:
            right.parent = self
        self.left: Optional['Node'] = left
        if left:
            left.parent = self
        self.key: int = key
        self.red: bool = red

    def get_child(self, is_left: bool):
        # if is_left is true will return left child, otherwise will return right child
        return self.left if is_left else self.right

    def set_child(self, is_left: bool, node: Optional['Node']):
        if is_left:
            self.left = node
        else:
            self.right = node

    def rotate(self, is_left: bool):
        # rotate left if is_left is true, else rotates right
        if self.get_child(not is_left):
            new_parent = self.get_child(not is_left)
            grandchild = new_parent.get_child(is_left)
            grandparent = self.parent
            self.set_child(not is_left, grandchild)
            if grandchild:
                grandchild.parent = self
            new_parent.parent = grandparent
            if grandparent:
                # fixup grandparent to point to rotated child, instead of
                if grandparent.get_child(True) == self:
                    # this was left child of grand parent
                    grandparent.set_child(True, new_parent)
                else:
                    grandparent.set_child(False, new_parent)
            self.parent = new_parent
            new_parent.set_child(is_left, self)
            return new_parent
        return self

    def rotate_left(self):
        return self.rotate(True)

    def rotate_right(self):
        return self.rotate(False)

    def insert(self, node: 'Node'):
        if node.key == self.key:
            raise RuntimeError(f"insert repeated key {node.key}")
        elif node.key < self.key:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self


def validate_connectivity(node: Node):
    if node.left:
        assert node.left.parent == node
        validate_connectivity(node.left)
    if node.right:
        assert node.right.parent == node
        validate_connectivity(node.right)


def validate_ordering(node: Node):
    if node.left:
        assert node.left.parent == node
        validate_ordering(node.left)
    if node.right:
        assert node.right.key > node.key
        validate_ordering(node.right)


def validate_coloring(node: Node, black_count=0, expected_black_count=None):
    if not node.red:
        black_count += 1
    if node.parent is None:
        # this is root node, it should not be red
        assert not node.red
    if node.left:
        expected_black_count = validate_coloring(node.left, black_count, expected_black_count)
        if node.red:
            assert not node.left.red
    if node.right:
        expected_black_count = validate_coloring(node.right, black_count, expected_black_count)
        if node.red:
            assert not node.right.red
    if not node.left or not node.right:
        if expected_black_count is not None:
            assert expected_black_count == black_count
        else:
            expected_black_count = black_count
    return expected_black_count


def validate_node_tree(node):
    validate_connectivity(node)
    validate_ordering(node)
    validate_coloring(node)


def fix_after_insert(node: Node, root: Node):
    # inserted node should be red
    assert node.red
    while node.parent and node.parent.red:
        # there are symetric cases for the parent being right or left of grandparent
        # instead of having two implementations, have just a single implementaton
        parent_is_left_child = node.parent == node.parent.parent.left
        node_is_left_child = node == node.parent.left
        alt_parent = node.parent.parent.right if parent_is_left_child else node.parent.parent.left
        alt_parent_is_red = (alt_parent is not None) and alt_parent.red
        # I'm guessing this shouldn't occur if tree is properly blanced after each insert
        if alt_parent_is_red:
            # CASE 1 (from video)
            # color parents black, and grand parents red
            alt_parent.red = False
            node.parent.red = False
            node.parent.parent.red = True
            # now see if grandparent is okay
            node = node.parent.parent
        elif parent_is_left_child != node_is_left_child:
            # alt parent is black
            # node and parents are on opposite sides
            parent = node.parent
            if parent == root:
                root = node
            parent.rotate(parent_is_left_child)
            # fix violation at node
            node = parent
        else:
            # alt parent is black,
            # and and parents are on same sides
            # if node is left child, rotate grandparent right
            node.parent.red = False
            node.parent.parent.red = True
            if node.parent.parent == root:
                root = node.parent
            node.parent.parent.rotate(not parent_is_left_child)
            # continue trying to "fix" tree from parent up
            node = node.parent

    if node.parent is None:
        # this is root, make it black
        node.red = False

    return root


def convert_tree_to_list(root: Node) -> List[int]:
    result = [root.key]
    level = [root]
    next_level = []
    while len(level):
        for node in level:
            if node.left:
                result.append(node.left.key)
                next_level.append(node.left)
            else:
                result.append(None)
            if node.right:
                result.append(node.right.key)
                next_level.append(node.right)
            else:
                result.append(None)
        level = next_level
        next_level = []
    while result and (result[-1] is None):
        result.pop()
    return result


def convert_list_to_tree(keys: List[int]):
    if len(keys) == 0:
        return None
    root = Node(keys[0])
    level = [root]
    next_level = []
    idx = 1
    while len(level):
        for node in level:
            if idx >= len(keys):
                break
            key = keys[idx]
            idx += 1
            if key is not None:
                new_node = Node(key, parent=node)
                node.left = new_node
                next_level.append(new_node)
            if idx >= len(keys):
                break
            key = keys[idx]
            idx += 1
            if key is not None:
                new_node = Node(key, parent=node)
                node.right = new_node
                next_level.append(new_node)
        level = next_level
        next_level = []

    return root


def print_node_tree(node: Optional[Node], indent=0):
    if indent > 10:
        print('  '*indent, "INDENT ERROR")
        return
    if node is not None:
        print_node_tree(node.right, indent+1)
        print('  '*indent, node.key, 'R' if node.red else 'B')
        print_node_tree(node.left, indent+1)


class Tree:
    """Red/Black Tree"""

    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key: int):
        new_node = Node(key)
        if self.root:
            self.root.insert(new_node)
        else:
            self.root = new_node
        self.root = fix_after_insert(new_node, self.root)

    def validate(self):
        if self.root:
            validate_node_tree(self.root)

    def convert_to_list(self) -> List[int]:
        return convert_tree_to_list(self.root)

    def print(self):
        if self.root:
            print_node_tree(self.root)
        else:
            print("EMPTY")


def key_permutations(keys, result=None):
    if result is None:
        result = []
    for idx, key in enumerate(keys):
        remaining_keys = keys[:idx] + keys[idx+1:]
        result.append(key)
        if len(remaining_keys):
            yield from key_permutations(remaining_keys, result)
        else:
            yield result
        result.pop()
