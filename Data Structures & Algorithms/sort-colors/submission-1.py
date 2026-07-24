class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # can use quicksort (three pointer method)
        # partition array and use two pointers
        # left pointer swaps everything with 0
        # right pointer swaps with 2
        # edge case if swapping with right pointer don't inc i
        # because swaps 0 into middle of array
        def swap(l, r):
            tmp = nums[r]
            nums[r] = nums[l]
            nums[l] = tmp
        
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1