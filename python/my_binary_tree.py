# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 06:45:55 2021

@author: Ham
Binary Tree Operations

https://pypi.org/project/binarytree/
Are you studying binary trees for your next exam,
assignment or technical interview?

Binarytree is a Python library which lets you generate, visualize,
inspect and manipulate binary trees.
Skip the tedious work of setting up test data,
and dive straight into practising your algorithms.
Heaps and BSTs (binary search trees) are also supported.

IPython Demo

Binarytree can be used with Graphviz (https://graphviz.org/)
and Jupyter Notebooks (https://jupyter.org/) as well:

Jupyter Demo

Requirements
Python 3.6+

Installation
Install via pip:

pip install binarytree
For conda users:

conda install binarytree -c conda-forge

"""

import operator
from binarytree import tree, bst, heap, Node

def binary_tree_level_order(node: Node) -> None:
    """
    An iterator to traverse a binary tree in "level" or "breadth first" order,
    returning each node's value -- one at a time.

    Args:
        node (Node): root of a binary tree.

    Yields:
        None

    Notes:
        1. To print all: print(*list(binary_tree_level_order(root)))
        2. This algorithm is non-recursive, single-pass so is very optimized.
           Time-complexity is probably O(2 * N) since each node is accessed
           twice: enque and deque. (Or, may be +3 for accessing its left,
           right children, and value.)
        3. To iterate from right-to-left, swap the lines for left<->right.
        4. The binarytree module already implements this traversal,
           so one can simply do:
               print(*[n.value for n in root.levelorder])
           Or slightly cooler:
               print(*map(operator.attrgetter('value'), root.levelorder))
        5. This is a popular interview coding question, which would ask an
           applicant to write his/her own code, so here it is.
        6. Weird bonus: to show it as a bottom-first, right-to-left:
               print(*list(binary_tree_level_order(root))[::-1])
    """

    queue = [node]
    while len(queue):
        node = queue.pop(0)
        yield node.value
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == '__main__':
    # Generate a random binary tree and return its root node.
    my_tree = tree(height=3, is_perfect=False)

    # Generate a random BST and return its root node.
    my_bst = bst(height=3, is_perfect=True)

    # Generate a random max heap and return its root node.
    my_heap = heap(height=3, is_max=True, is_perfect=False)

    # Pretty-print the trees in stdout.
    #print(my_tree)
    #print(my_bst)
    print(my_bst[12].value, my_bst[9].value, [my_bst[i].value for i in range(15)])
    del my_bst[9]
    #del my_bst[10]
    del my_bst[12]
    print(my_bst)
    #my_bst.pprint(index=True)
    print(my_bst.inorder)
    #print(my_bst.preorder)
    #print(my_bst.postorder)
    #print(*[n.value for n in my_bst.levelorder])
    print(*map(operator.attrgetter('value'), my_bst.levelorder))
    print(*binary_tree_level_order(my_bst))
    print(*list(binary_tree_level_order(my_bst))[::-1])
    #print(my_heap)

    #Build your own trees:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    #print(root[2].value)
    root.left.right = Node(4)

    #print(root)