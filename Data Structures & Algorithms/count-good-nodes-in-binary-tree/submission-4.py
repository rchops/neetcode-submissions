# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs with queue
        if not root:
            return 0        
        
        count = 1
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                if node.left.val >= node.val:
                    count += 1
                else:
                    node.left.val = node.val
                q.append(node.left)
                
            if node.right:
                if node.right.val >= node.val:
                    count += 1
                else:
                    node.right.val = node.val
                q.append(node.right)

        return count