"""
Root -> left -> right

usecase: Creating a copy of the tree, constructing an expression tree
"""

#Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(node, res):
    if not node:
        return

    

    # --- Pre-order Logic ---
    # Logic here processes 'root' BEFORE its children's results are fully handled.
    # This is where you might, for example, add root.val to a list,
    # or update a global/class variable based on root.val.
    # Example: print(root.val) # For pre-order traversal


    # Visit the current node first
    res.append(node.data)
    # Traverse the left subtree
    preOrder(node.left, res)

    # Traverse the right subtree
    preOrder(node.right, res)

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
    
    result = []
    preOrder(root, result)

    print(*result)

