#   There are 3 common graph representation structures:
#       - Edge List:
#           description: all pairs here represent edges in the graph for vertices with specific identifiers.
#           example: [(0,1), (0,2), (2,3), (1,4)]
#           pros: good for lookups of an edge or listing of all edges
#           cons: bad for most common usages like find all neighbour vertices ( it will cost O(N) here )
#       - Adjacency list:
#           description: for vertex at index i list[i] represent all it's adjacent vertices ( neighbours )
#           example: [[0,1,2], [3,4], [1]]
#           pros: constant time lookup for adjacent vertices, which is needed for most of path finding algorithms
#           cons: slow for edge operations
#       - Adjacency matrix:
#           description:  quadratic matrix of 0,1-s representing matrix[i][j]=1 as them being adjacent ( neighbours )
#           example: [[1,0,0],[0,0,1], [0, 1, 0]]
#           pros: good for edge lookups since we have constant time lookup for an edge.
#           cons: more space needed than other representations. Slow for listing all neighbours of some vertex
#


def edgesListToAdjacencyList(edges, type='directed'):
    def getNumberOfNodes():
        vertices = set()
        for start, to in edges:
            vertices.add(start)
            vertices.add(to)
        return len(vertices)
    adjList = [[] for _ in range(getNumberOfNodes())]
    for start, to in edges:
        adjList[start].append(to)
        if type == 'undirected':
            adjList[to].append(start)
    return adjList


result = edgesListToAdjacencyList([(0,1), (1,2), (2,3), (1,3)], 'undirected')
print(result)