"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

# Binary Tree Traversals
# DFS -> preorder, inorder, postorder
# BFS -> Level Order

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# print(root)
# print(root.left)
# print(root.right)


#Pre Order Traversal of Tree
def preOrder(root, arr):
    if root is None:
        return
    arr.append(root.val)
    preOrder(root.left, arr)
    preOrder(root.right, arr)
    return arr


result = preOrder(root, [])
print("Pre Order Traversal: ", result)

#In Order Traveral of Tree
def inOrder(root, arr):
    if root is None:
        return
    inOrder(root.left, arr)
    arr.append(root.val)
    inOrder(root.right, arr)
    return arr

result = inOrder(root, [])

print("In Order Traversal: ", result)


#Post Order Traversal
def postOrder(root, arr):
    if root is None:
        return
    postOrder(root.left, arr)
    postOrder(root.right, arr)
    arr.append(root.val)
    return arr

result = postOrder(root, [])

print("Post Order Traversal: ", result)