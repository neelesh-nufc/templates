class union_find:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return False
        
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        
        return True 