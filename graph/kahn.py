from collections import defaultdict, deque

def topo_sort_bfs(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    # Build graph and indegree count
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize queue with nodes having 0 indegree
    q = deque([i for i in range(n) if indegree[i] == 0])
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # If topo doesn't include all nodes → cycle exists
    if len(topo) != n:
        return []  # no valid topo order (cycle)
    
    return topo
