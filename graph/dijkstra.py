"""
| Use When                                 | Graph Type          | Edge Weights | Idea                                                                    |
| ---------------------------------------- | ------------------- | ------------ | ----------------------------------------------------------------------- |
| You need the shortest path from a source | Directed/Undirected | Non-negative | Greedily expand the shortest current node using a priority queue (heap) |


"""

import heapq
from collections import defaultdict

def dijkstra(n, edges, start):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(n)}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nei, w in graph[node]:
            if d + w < dist[nei]:
                dist[nei] = d + w
                heapq.heappush(heap, (dist[nei], nei))

    return dist
