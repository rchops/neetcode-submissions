# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs like level order but only take last num in level
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            new_level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                new_level.append(node.val)
            res.append(new_level[-1])
        
        return res