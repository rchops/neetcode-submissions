class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointer method
        # left and right pointer keeping track of max heights
        # move whichever pointer has smaller max
        # depending on side being moved L - height[i] for water held
        # only add if greater than 0
        l, r = 0, len(height) - 1
        rain = 0
        maxL, maxR = height[0], height[-1]
        while l < r:
            if maxL <= maxR:
                l += 1
                hold = maxL - height[l]
                if hold > 0:
                    rain += hold
                maxL = max(maxL, height[l])
            else:
                r -= 1
                hold = maxR - height[r]
                if hold > 0:
                    rain += hold
                maxR = max(maxR, height[r])
        
        return rain