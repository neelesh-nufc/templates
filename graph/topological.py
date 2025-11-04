"""
| Use When                                      | Graph Type                   | Idea                                               |
| --------------------------------------------- | ---------------------------- | -------------------------------------------------- |
| You need to order tasks based on dependencies | Directed Acyclic Graph (DAG) | Process nodes only when all prerequisites are done |

Graph must be directed and acyclic (DAG)
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = set()
        cycle = set()
        stack = []

        def dfs(node):
            if node in cycle:
                return False 

            if node in visited:
                return True
            
            cycle.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False 

            cycle.remove(node)
            visited.add(node)
            stack.append(node)

            return True 

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return stack