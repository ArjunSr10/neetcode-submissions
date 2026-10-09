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

        currentLevel = [root]

        while currentLevel:
            nextLevel = []
            for n in currentLevel:
                if n.left:
                    nextLevel.append(n.left)

                if n.right:
                    nextLevel.append(n.right)

                left = n.left
                n.left = n.right
                n.right = left
            
            currentLevel = nextLevel

        return root
        