from binarytree import build
from binarytree import Node as node
nodes = [3, 6, 8, 2, 11, None, 13]

binary_tree = build(nodes)
print('Binary tree from list :', binary_tree)
print('List from binary tree :', binary_tree.values)
print("Is Binary Tree Complete: ", binary_tree.is_complete)

print("-------------------------------------------------\nSecond Binary Tree implementation: ")
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
print("Binary Tree from adding nodes: ", root)
print("List from binary tree: ", root.values)
print("Is Binary Tree Complete: ", root.is_complete)
