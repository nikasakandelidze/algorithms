
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None"
        res = ""
        queue = []
        queue.append(root)
        res += str(root.val) + '|'
        while queue:
            temp = []
            while queue:
                v = queue.pop(0)
                if v.left: temp.append(v.left)
                if v.right: temp.append(v.right)
                res += 'None' if v.left is None else str(v.left.val)
                res += ','
                res += 'None' if v.right is None else str(v.right.val)
                if queue:
                    res += ':'
            if temp:
                res += '|'
            queue.extend(temp)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        1|2,3:|None,None:4,5:|None,None:None,None:|
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return None
        root = None
        prevs = []
        for s in data.split('|'):
            temp = []
            pairs = s.split(':')
            for pair in pairs:
                res = pair.split(',')
                if len(res) == 1:
                    root = TreeNode(res[0])
                    temp.append(root)
                else:
                    l, r = res
                    node = prevs.pop(0)
                    if not l == 'None':
                        ll = TreeNode(l)
                        node.left = ll
                        temp.append(ll)
                    else:
                        node.left = None
                    if not r == 'None':
                        rr = TreeNode(r)
                        node.right = rr
                        temp.append(rr)
                    else:
                        node.right = None
            prevs = temp
        return root


# Check mechanism
left_child = TreeNode("2")
right_child = TreeNode("3")
root = TreeNode("1", left_child, right_child)

codec = Codec()
result_string = codec.serialize(root)
print('serialized tree is:', result_string)

deserialized_root = codec.deserialize(result_string)
assert deserialized_root.val == root.val
assert deserialized_root.left.val == root.left.val
assert deserialized_root.right.val == root.right.val
print('all checks passed')

