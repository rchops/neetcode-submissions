class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums 
        # if already seen num skip
        # otherwise use two pointer to check if sum to 0
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
        

        return res