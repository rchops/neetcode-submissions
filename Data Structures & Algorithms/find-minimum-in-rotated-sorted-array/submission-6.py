class Solution:
    def findMin(self, nums: List[int]) -> int:
        # same as finding first true
        # first true is less than final val in array and smaller than everything after
        # it
        # standard binary search
        l, r = 0, len(nums) - 1
        target = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[-1]:
                target = m
                r = m - 1
            else:
                l = m + 1

        return nums[target]