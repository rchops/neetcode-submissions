class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # build set
        seen = set()
        for num in nums:
            seen.add(num)

        # go through array again and check if num-1 exists in set
        # if does move on till doesn't to find start of seq
        # after finding start of seq see how many cons vals are in set

        i = 0
        max_len = 0
        for i in range(len(nums)):
            cons = 0
            if nums[i]-1 in seen:
                i += 1
            else:
                idx = nums[i]
                while idx in seen:
                    idx += 1
                    cons += 1
            
            if cons > max_len:
                max_len = cons

        return max_len