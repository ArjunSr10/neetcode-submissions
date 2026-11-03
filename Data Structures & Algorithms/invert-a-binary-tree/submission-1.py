# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = root
        if not root:
            return None

        queue = collections.deque([root])

        while queue:
            qLen = len(queue)
            for i in range(qLen):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp = node.left
                node.left = node.right
                node.right = tmp

        return dummy


                