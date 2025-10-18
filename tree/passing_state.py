"""
you might need to pass additional parameters to your recursive function to maintain state.
e.g current_sum, current_path, min_val_so_far, parent_node, etc
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, current_sum, current_path):
    if not node:
        return
    
    current_path.append(node.val)
    current_sum += node.val

    if not node.left and not node.right:
        # This is a leaf node, so we process the completed path
        print(f'Path: {current_path}, Sum: {current_sum}')

    dfs(node.left, current_sum, current_path)
    dfs(node.right, current_sum, current_path)

    # Backtrack: remove the current node from the path before returning,
    # so it doesn't affect sibling paths.
    current_path.pop()

if __name__ == "__main__":
    # Create a binary tree for testing
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    root = TreeNode(5)
    root.left = TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2)))
    root.right = TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1)))

    print("Finding all root-to-leaf paths and their sums:")
    # Initial call starts with a sum of 0 and an empty path list
    dfs(root, 0, [])
