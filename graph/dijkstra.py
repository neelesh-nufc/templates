"""
| Use When                                 | Graph Type          | Edge Weights | Idea                                                                    |
| ---------------------------------------- | ------------------- | ------------ | ----------------------------------------------------------------------- |
| You need the shortest path from a source | Directed/Undirected | Non-negative | Greedily expand the shortest current node using a priority queue (heap) |

Purpose: Finds the shortest paths from a single source node to all other nodes in a weighted graph with non-negative edge weights.

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

# Network delay time 

import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        time = 0

        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue 
            
            visited.add(node)
            time = dist

            for v, w in graph[node]:
                heapq.heappush(heap, (dist + w, v))
        
        return time if len(visited) == n else -1
                