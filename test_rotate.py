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

from rbtree import (Node, convert_tree_to_list, convert_list_to_tree,
                    print_node_tree, validate_connectivity)


def test_rotate_left():
    tree = convert_list_to_tree([1, 2, 3])
    print("orig tree")
    print_node_tree(tree)
    tree = tree.rotate_left()
    print("rotated tree")
    print_node_tree(tree)
    key_list = convert_tree_to_list(tree)
    assert key_list == [3, 1, None, 2]
    validate_connectivity(tree)


def test_rotate_right():
    tree = convert_list_to_tree([1, 2, 3])
    print("orig tree")
    print_node_tree(tree)
    tree = tree.rotate_right()
    print("rotated tree")
    print_node_tree(tree)
    key_list = convert_tree_to_list(tree)
    assert key_list == [2, None, 1, None, 3, ]
    validate_connectivity(tree)


def test_rotate_subtree_left():
    subtree = convert_list_to_tree([1, 2, 3])
    tree = Node(10, left=subtree)
    print("orig tree")
    print_node_tree(tree)
    subtree.rotate_left()
    print("rotated tree")
    print_node_tree(tree)
    key_list = convert_tree_to_list(tree)
    assert key_list == [10, 3, None, 1, None, 2]
    validate_connectivity(tree)


def test_rotate_subtree_right():
    subtree = convert_list_to_tree([1, 2, 3])
    tree = Node(10, left=subtree)
    print("orig tree")
    print_node_tree(tree)
    subtree.rotate_right()
    print("rotated tree")
    print_node_tree(tree)
    key_list = convert_tree_to_list(tree)
    assert key_list == [10, 2, None, None, 1, None, 3]
    validate_connectivity(tree)
