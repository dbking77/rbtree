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

from rbtree import (Tree, key_permutations)


def test_insert_list1():
    tree = Tree()
    for key in [1, 2]:
        tree.insert(key)
    tree.validate()
    result = tree.convert_to_list()
    assert result == [1, None, 2]


def test_insert_list2():
    tree = Tree()
    for key in [1, 2, 3]:
        tree.insert(key)
        tree.validate()
    result = tree.convert_to_list()
    assert result == [2, 1, 3]


def test_insert_list3():
    tree = Tree()
    for key in [1, 3, 2]:
        tree.insert(key)
        tree.validate()
    result = tree.convert_to_list()
    assert result == [2, 1, 3]


def test_insert_list_all3():
    for keys in ([1, 2, 3], [1, 3, 2], [2, 3, 1], [2, 1, 3], [3, 1, 2], [3, 2, 1]):
        print("keys", keys)
        tree = Tree()
        for key in keys:
            tree.insert(key)
            tree.validate()
        result = tree.convert_to_list()
        assert result == [2, 1, 3]


def test_insert_list_all4():
    for keys in key_permutations([1, 2, 3, 4]):
        print("keys", keys)
        tree = Tree()
        for key in keys:
            tree.insert(key)
            tree.validate()
        print("tree final")
        tree.print()
