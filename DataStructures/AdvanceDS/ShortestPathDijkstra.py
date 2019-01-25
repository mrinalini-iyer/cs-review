# Shortest distance suing adjacency matrix
import sys

class Graph():
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        
    def printDistance(self, dist):
        
        for index in range(self.V):
            print(index ,":", dist[index])
            
            
    # Return the index of the vertix that is not in the shortest path list
    # but has the minimum distance
    def minDistance(self, visited, dist):
        
        min_dist = sys.maxsize
        
        for index in range(self.V):
            if visited[index] == False and dist[index] < min_dist:
                min_dist = dist[index]
                min_index = index
                
        return min_index
    
    # Find the distance from the src to any of the other nodes in the graph
    def dijkstra(self, src):
        # initialize all the nodes with infinity
        dist  = [sys.maxsize] * self.V
        # Set the source distance to 0
        dist[src] = 0
        # Set all the nodes in the sptSet to False
        visited = [False]* self.V
        
        for index in range(self.V):
            # pick up the vertix with the minimum distance from the dist list
            # initially the src node is 0 and is returned
            u = self.minDistance(visited, dist)
        
            # Add the minimum distance node to the shortest path set 
            visited[u] = True
            
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    
        
        return dist
                

# Test shortest path 
g = Graph(9)

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 

dist = g.dijkstra(0)

g.printDistance(dist)
    

