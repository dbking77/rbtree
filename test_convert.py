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


def test_convert_tree_to_list1():
    n8 = Node(8)
    n5 = Node(5, left=n8)
    n6 = Node(6)
    n3 = Node(3, left=n5, right=n6)
    n9 = Node(9)
    n4 = Node(4, right=n9)
    n2 = Node(2, left=n3, right=n4)
    result = convert_tree_to_list(n2)
    assert result == [2, 3, 4, 5, 6, None, 9, 8]


def test_convert_tree_to_list2():
    n1 = Node(1)
    n2 = Node(2, left=n1)
    n5 = Node(5)
    n4 = Node(4, right=n5)
    n3 = Node(3, left=n2, right=n4)
    print_node_tree(n3)
    result = convert_tree_to_list(n3)
    assert result == [3, 2, 4, 1, None, None, 5]


def test_convert_bidir1():
    list1 = [2, 3, 4, 5, 6, None, 9, 8]
    tree = convert_list_to_tree(list1)
    validate_connectivity(tree)
    list2 = convert_tree_to_list(tree)
    assert list2 == list1


def test_convert_bidir2():
    list1 = [3, 2, 4, 1, None, None, 5]
    tree = convert_list_to_tree(list1)
    validate_connectivity(tree)
    list2 = convert_tree_to_list(tree)
    assert list2 == list1
