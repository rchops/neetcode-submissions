class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix and suffix array
        # go left to right through array and multiply as go along for prefix array
        # go right to left through array and multiply as go along for suffix array
        prefix = [1]
        for i in range(1,len(nums)):
            prefix.append(nums[i-1] * prefix[i-1])

        suffix = [1]
        rev_nums = list(reversed(nums))
        for i in range(1, len(nums)):
            suffix.append(rev_nums[i-1] * suffix[i-1])

        suffix = list(reversed(suffix))

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res