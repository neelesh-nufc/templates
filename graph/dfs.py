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

def dfs(node):
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            dfs(nei)

visited = set()
for node in graph:
    if node not in visited:
        dfs(node)
