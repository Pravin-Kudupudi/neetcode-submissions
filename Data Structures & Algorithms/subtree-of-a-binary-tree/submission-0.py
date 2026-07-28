# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()
            if self.isSametree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False
    

    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        
        if (p is None and q is not None) or (p is not None and q is None) or p.val != q.val:
            return False

        if p.val == q.val:
            return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)