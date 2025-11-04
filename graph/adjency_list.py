from collections import defaultdict

graph = defaultdict(list)
for u, v, w in edges:  # weighted
    graph[u].append((v, w))
    graph[v].append((u, w))  # omit for directed graph
