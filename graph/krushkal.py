"""
| Use When                        | Graph Type          | Edge Weights | Idea                                                  |
| ------------------------------- | ------------------- | ------------ | ----------------------------------------------------- |
| You want MST using disjoint set | Undirected Weighted | Any          | Sort edges by weight and union nodes if not connected |

"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    parent[ry] = rx
    return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    global parent
    parent = [i for i in range(n)]
    total = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
    return total

