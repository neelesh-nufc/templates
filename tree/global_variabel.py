"""
Sometimes, it's easier to use a global variable to accumulate results
that don't need to be passed up recursion stack. like: list all node valeues, running sum, etc
"""

#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # It's better practice to initialize instance variables in the constructor.
        self.max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(node, current_depth):
            if not node:
                return

            # Update the global maximum if the current node is a leaf or just at a deeper level
            self.max_depth = max(self.max_depth, current_depth)

            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        dfs(root, 1)
        return self.max_depth

if __name__ == "__main__":
    # Create a binary tree for testing
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solver = Solution()
    depth = solver.maxDepth(root)
    print(f"The maximum depth of the tree is: {depth}") # Expected output: 3