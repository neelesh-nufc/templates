"""
| Use When                                               | Graph Type          | Edge Weights | Idea                                                                           |
| ------------------------------------------------------ | ------------------- | ------------ | ------------------------------------------------------------------------------ |
| You want a tree connecting all nodes with minimum cost | Undirected Weighted | Any          | Greedily grow MST by always adding the smallest edge that connects to new node |

"""

import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    heap = [(0, 0)]  # (weight, start_node)
    total_cost = 0

    while heap and len(visited) < n:
        w, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += w
        for nei_w, nei in graph[u]:
            if nei not in visited:
                heapq.heappush(heap, (nei_w, nei))
    return total_cost



