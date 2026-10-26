# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs both at same time and if not same return false

        def bfs(p, q):
            pQ = deque([p])
            qQ = deque([q])

            while pQ and qQ:
                pCurr = pQ.popleft()
                qCurr = qQ.popleft()

                if pCurr is None and qCurr is None:
                    continue

                if pCurr is None or qCurr is None:
                    return False

                if pCurr.val != qCurr.val:
                    return False
                
                for pChild in [pCurr.left, pCurr.right]: 
                        pQ.append(pChild)

                for qChild in [qCurr.left, qCurr.right]:
                        qQ.append(qChild)

            return True

        return bfs(p,q)