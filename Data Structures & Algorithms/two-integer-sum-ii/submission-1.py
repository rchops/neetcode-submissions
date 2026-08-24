class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointer
        # start either side - less than target move left, more than target move right
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1