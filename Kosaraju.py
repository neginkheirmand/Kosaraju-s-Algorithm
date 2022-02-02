# Kusaraju's Algorithm to find Strongly Connected Componnents(SCC) using a DFS approach 



visited = {}
ListOfVertices = [] # An ordered list of vertices
SCC = {} # dictinary of (key = vertex ,value = rootVertex) values

graph = {}

def addEdge(v1 , v2):
    
    if graph.get(v1) is None:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)
        
    if graph.get(v2) is None:
        graph[v2] = []

def getNeighbors(v):
    return graph[v]

def getInNeighbors(v):
    neighbors =[]
    for n in graph.keys():
        if v in graph[n] :
            neighbors.append(n)
    return neighbors

def visit(v):
    if visited[v] is False:
        visited[v] = True
        for n in getNeighbors(v):
            visit(n)
        ListOfVertices.append(v)
    else:
        pass


def putInComponent(v, c):
    if v in SCC.keys():
        pass
    else:
        SCC[v] = c
        for n in getInNeighbors(v):
            putInComponent(n,c)


def findSCC():
    
    #Mark all vertices unvisited
    for v in graph.keys():
        visited[v] = False
    
    #Visit all vetices
    for v in graph.keys():
        visit(v)
    
    #Segmentation
    for v in reversed(ListOfVertices):
        putInComponent(v,v)
    
    res = {}
    for c ,vs in SCC.items():
        res[vs] = [c] if vs not in res.keys() else res[vs] + [c]
    
    StrongConnectedComponents = []
    for c in res.keys():
        StrongConnectedComponents.append(res[c])
    return StrongConnectedComponents   

# testing with values
# test 1
addEdge(0,1)
addEdge(1,2)
addEdge(2,0)
addEdge(2,3)
addEdge(3,4)
addEdge(2,5)
addEdge(5,6)
addEdge(6,7)
addEdge(7,5)
addEdge(7,8)
addEdge(8,6)

res = findSCC()

    
    
print(res,"\n\n\n")


visited.clear()
ListOfVertices.clear()
SCC.clear()
graph.clear()
res.clear()
# testing with values
# test 2
addEdge(0,1)
addEdge(1,2)
addEdge(2,3)
addEdge(3,4)

res = findSCC()

    
    
print(res,"\n\n\n")


visited.clear()
ListOfVertices.clear()
SCC.clear()
graph.clear()
res.clear()
# testing with values
# test 2
addEdge(0,1)
addEdge(1,2)
addEdge(2,3)
addEdge(3,4)
addEdge(4,3)
addEdge(3,2)
addEdge(2,1)
addEdge(1,0)

res = findSCC()

    
    
print(res,"\n\n\n")

visited.clear()
ListOfVertices.clear()
SCC.clear()
graph.clear()
res.clear()
# testing with values
# test 2
addEdge(0,1)
addEdge(1,2)
addEdge(2,3)
addEdge(2,4)
addEdge(3,0)
addEdge(4,5)
addEdge(5,6)
addEdge(6,4)
addEdge(6,7)


res = findSCC()

    
    
print(res,"\n\n\n")





            