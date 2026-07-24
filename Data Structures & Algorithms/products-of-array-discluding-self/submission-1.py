class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix and suffix array
        # multiplying at index i gives product without i
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        rev_nums = list(reversed(nums))
        for i in range(1, len(nums)):
            suffix[i] = suffix[i-1] * rev_nums[i-1]
        
        suffix = list(reversed(suffix))

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res
        