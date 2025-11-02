"""
Depth-First Search (DFS) is a traversal algorithm used to explore nodes & edges of a graph
as far as possible along each branch before backtracking.

➡️ Go deep into one path until you can’t go further,
➡️ then backtrack and explore other paths.

Used For:

Counting connected components
Finding reachable nodes
Shortest path in unweighted graphs
"""


# Number of island 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # base condition: out of bounds, already visited, or water
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0' or
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    total_islands += 1
        
        return total_islands

