class Solution(object):
    # Since grapth is acyclic and uni-directional we don't need visited ?

    # start iterating over the adjList
    # lets store in the visited and stack structures path(list of sequential node values like: [0 1 2])
    # On each iteration take last element(node) of the path list.
    # find it's neighbours, and append each of them to path by creating new copy of new path
    # add this newly generated paths to stack
    def allPathsSourceTarget(self, graph):
        adjList = graph
        stack = [[0]]
        result = []
        while stack:
            path = stack.pop(0)
            if path[-1] == len(graph) - 1:
                result.append(path)
            neighbours = adjList[path[-1]]
            for n in neighbours:
                new_path = path[:]
                new_path.append(n)
                stack.append(new_path)
        return result

