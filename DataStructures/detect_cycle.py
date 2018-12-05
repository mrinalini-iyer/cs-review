from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdges(self, u, v):
        self.graph[u].append(v)
    
    def dfsUtil(self, v, visited, parent):
        visited[v] = True
        #print(v)
        
        for i in self.graph[v]:
            if visited[i] == False:
                if self.dfsUtil(i, visited, v) == True:
                    return True
            else:
                if parent != i:
                    return True
            
        
        return False
    
    def DFS(self, v):
        
    
        visited = [False] * len(self.graph)
        
        self.dfsUtil(v, visited)
        
    def is_cycle(self):
        visited = [False] * len(self.graph)
        
        for i in self.graph:
            if visited[i] == False:
                if self.dfsUtil(i, visited, -1) == True:
                    print("cycle detected")
                    return True
        return False
                
        
        

# Test
g = Graph()
g.addEdges(0,2)
g.addEdges(2,3)
g.addEdges(3,1)
g.addEdges(1, 3)
g.addEdges(2,2)

#g.DFS(2)
g.is_cycle()
