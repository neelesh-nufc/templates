"""
| Use When                                      | Graph Type                   | Idea                                               |
| --------------------------------------------- | ---------------------------- | -------------------------------------------------- |
| You need to order tasks based on dependencies | Directed Acyclic Graph (DAG) | Process nodes only when all prerequisites are done |

Graph must be directed and acyclic (DAG)
"""

from collections import defaultdict

def topo_sort_dfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []      # to store topological order
    cycle = set()   # for cycle detection (optional)

    def dfs(node):
        if node in cycle:
            raise ValueError("Cycle detected!")  # or return []
        if node in visited:
            return

        cycle.add(node)
        for nei in graph[node]:
            dfs(nei)
        cycle.remove(node)

        visited.add(node)
        stack.append(node)

    for node in range(n):
        if node not in visited:
            dfs(node)

    stack.reverse()
    return stack

