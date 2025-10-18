"""
While recursion is common, an iterative approach using an explicit stack can be used,
especially to avoid recursion depth limits for very deep trees.
DFS uses Stack -> this is DFS
BFS uses Queue
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iterative_dfs_preorder(root):
    if not root:
        return

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right child first, then left child, so that when we pop,
        # the left child is processed before the right child (pre-order).
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

if __name__ == "__main__":
    # Create a binary tree for testing
    #       1
    #      /  \
    #    2     3
    #   / \     \
    #  4   5     6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Performing iterative pre-order DFS...")
    traversal_result = iterative_dfs_preorder(root)

    print(f"Tree structure: 1 -> (2 -> (4, 5)), (3 -> (None, 6))")
    print(f"Pre-order traversal result: {traversal_result}") # Expected: [1, 2, 4, 5, 3, 6]