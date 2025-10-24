"""
| Use When                                      | Graph Type                   | Idea                                               |
| --------------------------------------------- | ---------------------------- | -------------------------------------------------- |
| You need to order tasks based on dependencies | Directed Acyclic Graph (DAG) | Process nodes only when all prerequisites are done |

"""

def topo_dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            topo_dfs(nei)
    stack.append(node)

stack, visited = [], set()
for node in graph:
    if node not in visited:
        topo_dfs(node)

topo_order = stack[::-1]
