# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #   find path to each of nodes. start finding lowest matching node.val in these paths
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q, result):
            if root is None:
                return (False, False)
            if root is p or root is q:
                newp, newq = None, None
                if root is p:
                    if q is None:
                        return (True, False)
                    newq = q
                if root is q:
                    if p is None:
                        return (False, True)
                    newp = p
                lpfound, lqfound = helper(root.left, newp, newq, result)
                rpfound, rqfound = helper(root.right, newp, newq, result)
                if root is p and (lqfound or rqfound):
                    if not result[0]:
                        result[0] = root
                if root is q and (rpfound or lpfound):
                    if not result[0]:
                        result[0] = root
                return (root is p, root is q)
            else:
                fp1, fq1 = helper(root.left, p, q, result)
                fp2, fq2 = helper(root.right, p, q, result)
                if (fp1 and fq2) or (fp2 and fq1):
                    if not result[0]:
                        result[0] = root
                return (fp1 or fp2, fq1 or fq2)
        result = [None]
        helper(root, p, q, result)
        return result[0]