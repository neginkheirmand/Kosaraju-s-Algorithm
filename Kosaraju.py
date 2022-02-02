# Kusaraju's Algorithm to find Strongly Connected Componnents(SCC) using a DFS approach 



visited = [] 
ListOfVertices = [] # An ordered list of vertices
SCC = {} # dictinary of (key = vertex ,value = rootVertex) values

graph = {}

def addEdge(v1 , v2):
    if graph.get(v1) is None:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)

def getNeighbors(v):
    return graph[v]
    

def visit(v):
    if visited[v] is False:
        visited[v] = True
        for n in getNeighbors(v):
            visit(n)
        ListOfVertices.append(v)
    else:
        pass


def findSCC():
    
    #Mark all vertices unvisited
    visited = [False * len(graph)]
            