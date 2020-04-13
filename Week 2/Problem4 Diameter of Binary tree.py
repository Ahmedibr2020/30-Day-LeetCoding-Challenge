""" Diameter of Binary Tree
    Given a binary tree, you need to compute the length
    of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path
    between any two nodes in a tree.
    This path may or may not pass through the root.
    Ahmed Ibrahim 
    """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ret = 0
        def getDepth(root):
            if not root:
                return 0
            L = getDepth(root.left)
            R = getDepth(root.right)
            self.ret = max(self.ret, 1 + L + R)
            return 1 + max(L, R)
        getDepth(root)
        return self.ret - 1
