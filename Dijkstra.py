import sys
class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(self.V)] for row in range(self.V)]
    def minDist(self,dist,spaSet):
        min=8575545699
        for i in range(self.V):
            if(dist[i]<min and spaSet[i]==False):
                min=dist[i]
                min_index=i
        return min_index
    def dijkstra(self,src):
        dist=[844558555]*self.V
        dist[src]=0
        spaSet=[False]*self.V

        for i in range(self.V):
            u=self.minDist(dist,spaSet)
            spaSet[u]=True
            
            for m in range(self.V):
                if self.graph[u][m]>0 and spaSet[m]==False and dist[m]>dist[u]+self.graph[u][m]:
                    dist[m]=dist[u]+self.graph[u][m]
