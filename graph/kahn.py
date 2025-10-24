from collections import deque

indegree = {u: 0 for u in graph}
for u in graph:
    for v in graph[u]:
        indegree[v] += 1

queue = deque([u for u in graph if indegree[u] == 0])
res = []
while queue:
    node = queue.popleft()
    res.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)
