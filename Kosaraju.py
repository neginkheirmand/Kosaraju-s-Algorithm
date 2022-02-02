# Kusaraju's Algorithm to find Strongly Connected Componnents(SCC) using a DFS approach 



visited = {} 
ListOfVerteces = [] # An ordered list of vertices
SSC = {} # dictinary of (key = vertex ,value = rootVertex) values

graph = {}

def addEdge(v1 , v2):
    if graph.get(v1) is None:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)

def getNeighbors(v):
    return graph[v]
    