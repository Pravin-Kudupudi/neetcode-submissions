# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        visited = deque([root])

        while visited:
            current = visited.pop()
            if current.left:
                visited.append(current.left) 
            if current.right:
                visited.append(current.right) 
            current.left, current.right = current.right, current.left

        return root