"""
left -> right -> root

usecae: deleting node in a tree (ensuring children are deleted before parent), calculating disk space used by dir
"""

# Node Structure
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def postOrder(node, res):
    if node is None:
        return
    
    # --- Post-order Logic ---
    # Logic here processes 'root' AFTER both children's results are returned.
    # This is common for problems that need information from children to decide on the parent,
    # e.g., calculating subtree sum, height, max path sum.
    # Example: return root.val + left_result + right_result # For subtree sum

    # First we traverse left subtree
    postOrder(node.left, res)

    # After visiting left, traverse right subtree
    postOrder(node.right, res)

    # now we visit node
    res.append(node.data)

if __name__ == "__main__":
    #Represent Tree
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    result = []
    postOrder(root, result)

    # Print the postorder
    for val in result:
        print(val, end=" ")