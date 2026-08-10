class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep max counter
        # if left bigger move right pointer
        # if right bigger move left pointer
        most = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            current = height * (r - l)
            most = max(current, most)
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return most