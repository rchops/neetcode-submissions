class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # use mergesort
        # first break array into smaller halves
        # split halfway, do mergeSort on smaller halves
        # then merge using two pointer

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m) # left
            mergeSort(arr, m + 1, r) # right
            merge(arr, l, m, r) # merge everything back together
            return arr

        l, r = 0, len(nums) - 1
        return mergeSort(nums, l, r)