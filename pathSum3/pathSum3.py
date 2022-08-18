from typing import Optional


# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchHelper(self, root, targetSum, counter, tempSum):
        new_sum = tempSum + root.val
        if new_sum == targetSum:
            counter[0] += 1
        if root.left:
            self.searchHelper(root.left, targetSum, counter, new_sum)
        if root.right:
            self.searchHelper(root.right, targetSum, counter, new_sum)

    def traverse(self, root, targetSum, counter):
        if root is not None:
            self.searchHelper(root, targetSum, counter, 0)
            if root.left:
                self.traverse(root.left, targetSum, counter)
            if root.right:
                self.traverse(root.right, targetSum, counter)
        return counter

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = [0]
        return self.traverse(root, targetSum, counter)[0]


t1 = TreeNode(1, TreeNode(2, TreeNode(1), TreeNode(1)), TreeNode(3))
solution = Solution()
result = solution.pathSum(t1, 3)
assert result == 4