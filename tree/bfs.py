"""
Why BFS: Level order traversal, finding minimum depth/height, finding the closest node, etc.
This specific implementation finds the minimum depth of a binary tree.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if not root:
        return 0 # An empty tree has a depth of 0.

    # Use a deque for efficient appends and pops from both ends (O(1) time complexity).
    # Using list.pop(0) is inefficient (O(n) time complexity).
    queue = deque([root])
    level = 0

    while queue:
        level += 1
        # Process all nodes at the current level
        for _ in range(len(queue)):
            node = queue.popleft() # Dequeue from the front

            # If we find a leaf node, this is the shortest path from the root.
            if not node.left and not node.right:
                return level

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level # Should not be reached in a non-empty tree, but good for completeness.

if __name__ == "__main__":
    # Create a binary tree for testing
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

    min_depth = bfs(root)
    # The first leaf node encountered is '9' at level 2.
    print(f"The minimum depth of the tree is: {min_depth}") # Expected output: 2
