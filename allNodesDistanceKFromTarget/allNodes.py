from typing import Tuple
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#   Start searching for the node
#       If you find a node start searching down in the sub-tress for k distanced ones.
#       Also return true when returning from the target node so that upper level nodes
#           know that they should also start counting

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        graph=defaultdict(lambda:[]) # node.val: [neighbour_nodes]
        def fill_graph(node: TreeNode, parent_node: TreeNode):
            if node is None:
                return
            ls = graph[node.val]
            if parent_node is not None:
                ls.append(parent_node.val)
            if node.left:
                ls.append(node.left.val)
                fill_graph(node.left, node)
            if node.right:
                ls.append(node.right.val)
                fill_graph(node.right, node)
        fill_graph(root, None)
        result = []
        target_node_neighbours = graph[target.val]
        neighbours = [(x,1) for x in target_node_neighbours]
        visited = {target.val}
        for x in neighbours:
            visited.add(x[0])
        while len(neighbours)>0:
            value, distance = neighbours.pop()
            if distance == k:
                result.append(value)
            for n in graph[value]:
                if n not in visited:
                   neighbours.append((n, distance+1))
                   visited.add(n)
        return result

                




