class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # can use prefix and suffix array
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        ans = [1] * len(nums)
        # prefix is prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        # reverse nums for suffix
        nums_rev = list(reversed(nums))
        for i in range(1, len(nums_rev)):
            suffix[i] = nums_rev[i-1] * suffix[i-1]

        suffix = list(reversed(suffix))

        for i in range(len(ans)):
            ans[i] = prefix[i] * suffix[i]

        return ans