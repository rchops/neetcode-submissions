from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use sliding window with queue
        # add largest element to right compare elements and remove if smaller (.pop)
        # add to ans from left (.popleft)
        ans = []
        maxQ = deque()
        l = 0

        for r in range(k):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[r])

        ans.append(maxQ[0])  

        for r in range(k, len(nums)):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            
            maxQ.append(nums[r])
            if nums[l] == maxQ[0]:
                maxQ.popleft()
            
            l += 1
            ans.append(maxQ[0])
        
        return ans