"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        clonedNodes = {node.val: Node(node.val, [])}
        stack = [node]
        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor.val not in clonedNodes.keys():
                    new_node = Node(neighbor.val, [])
                    clonedNodes[n.val].neighbors.append(new_node)
                    clonedNodes[new_node.val] = new_node
                    stack.append(neighbor)
                else:
                    clonedNeighbor = clonedNodes[neighbor.val]
                    clonedCurrentNode = clonedNodes[n.val]
                    if clonedNeighbor.val not in clonedCurrentNode.neighbors:
                        clonedCurrentNode.neighbors.append(clonedNeighbor)
        return clonedNodes[node.val]

