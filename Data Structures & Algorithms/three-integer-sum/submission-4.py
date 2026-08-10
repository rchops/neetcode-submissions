class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array
        nums_sorted = nums.sort()

        # have one pointer walk through array
        # two pointers left and right find if add to 0
        # move right if too large move left if too small
        # if already seen first num then skip
        seen = set()
        ans = []
        for i, num in enumerate(nums):
            if num in seen:
                continue
            l, r = i + 1, len(nums) - 1
            seen_l = set()
            seen_r = set()
            while l < r:
                if nums[l] in seen_l and nums[r] in seen_r:
                    r -= 1
                elif num + nums[l] + nums[r] == 0:
                    ans.append([num, nums[l], nums[r]])    
                    seen.add(num)
                    seen_l.add(nums[l])
                    seen_r.add(nums[r])
                    r -= 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return ans