class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search to split array into halves and then update pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # checking left sorted part
            elif nums[mid] >= nums[l]:
                # would check right if target > mid or target < l
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # checking right sorted part
            else:
                # would check left if target < mid or target > r
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
