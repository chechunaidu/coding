from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def isConnected(self,s,d):
        visited=[False]*self.V
        queue=[]
        queue.append(s)
        while queue:
            n=queue.pop(0)
            if n==d:
                return True
            for i in self.graph[n]:
                if (visited[i]==False):
                    queue.append(i)
                    visited[i]=True
        return False
