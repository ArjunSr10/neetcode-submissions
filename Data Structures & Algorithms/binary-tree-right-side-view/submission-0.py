# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        queue = collections.deque([root])

        while queue:
            qLen = len(queue)
            for i in range(qLen - 1):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rightNode = queue.popleft()
            res.append(rightNode.val)

            if rightNode.left:
                queue.append(rightNode.left)

            if rightNode.right:
                queue.append(rightNode.right)

        return res
            