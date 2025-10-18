"""
left -> right -> root

usecase: BST, in-order traversal visites nodes in non decresing order
"""

#Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def inOrder(node, res):
    if node is None:
        return
    
    # --- In-order Logic --- (Binary Trees only)
    # Logic here processes 'root' AFTER left child, BEFORE right child.
    # Example: print(left_result, root.val, right_result)

    # Traverse the left subtree first
    inOrder(node.left, res)

    # Visit the current node
    res.append(node.data)

    # Traverse the right subtree last
    inOrder(node.right, res)

if __name__ == "__main__":
    # Create binary tree
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    res = []
    inOrder(root, res)

    for node in res:
        print(node, end=" ")