class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap with num as key, idx as val
        # if in hashmap return otherwise add
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []