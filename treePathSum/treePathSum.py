from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    # DFS solution
    def _recursiveHelper(self, root, targetSum, currentSum, currentList, resultLists):
        if root is None:
            return
        elif (not root.left and not root.right):
            if currentSum + root.val == targetSum:
                currentList.append(root.val)
                resultLists.append(currentList)
        else:
            if root.left:
                copy1 = currentList[:]
                copy1.append(root.val)
                self._recursiveHelper(root.left, targetSum, currentSum + root.val, copy1, resultLists)
            if root.right:
                copy2 = currentList[:]
                copy2.append(root.val)
                self._recursiveHelper(root.right, targetSum, currentSum + root.val, copy2, resultLists)

    # BFS solution
    def _bfsHelper(self, root, targetSum):
        if root is None:
            return []
        result = []
        queue = []
        queue.append((root, [root.val]))
        while queue:
            node, listOfNodes = queue.pop(0)
            if not node.left and not node.right:
                if sum(listOfNodes) == targetSum:
                    result.append(listOfNodes)
            else:
                if node.left:
                    nextListOfNodes = listOfNodes[:]
                    nextListOfNodes.append(node.left.val)
                    queue.append((node.left, nextListOfNodes))
                if node.right:
                    nextListOfNodes = listOfNodes[:]
                    nextListOfNodes.append(node.right.val)
                    queue.append((node.right, nextListOfNodes))
        return result

    def pathSum(self, root: Optional[TreeNode], targetSum: int, type='bfs') -> List[List[int]]:
        if type == 'dfs':
            result = []
            self._recursiveHelper(root, targetSum, 0, [], result)
            return result
        elif type == 'bfs':
            return self._bfsHelper(root, targetSum)


t1 = TreeNode(1)
t2 = TreeNode(4)
t3 = TreeNode(3, t1, t2)
t4 = TreeNode(5)
t5 = TreeNode(7)
t6 = TreeNode(2, t4, t5)
t7 = TreeNode(-6, t3, t6)

solution = Solution()
result = solution.pathSum(t7, 1)
print(result)
assert len(result) == 2