class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search to split array into halves and then update pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left sorted part - if greater than left most val means that its not past 
            # the smallest num
            elif nums[mid] >= nums[l]:
                # would check right if target > mid or target < l
                # if greater than mid - then is to the right of the left sorted part
                # if less than nums[l] then in the right sorted part
                # both cases l = mid + 1
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right sorted part - otherwise greater than the smallest val
            else:
                # would check left if target < mid or target > r
                # if less than mid - then is to the left of the right sorted part
                # if greater than nums[r] then in left sorted part
                # both cases r = mid - 1
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
