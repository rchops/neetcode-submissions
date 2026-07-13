class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # use mergesort
        # split array into half each time then re-merge with two pointer
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1] # inclusive left, exclusive right
            i, j, k = L, 0, 0 # for walking through arrays

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
                i += 1
                j += 1
            while k < len(right):
                arr[i] = right[k]
                i += 1
                k += 1
        
        def mergeSort(arr, l, r):
            # base case for recursion
            # size of 1
            if l == r:
                return arr

            m = (l + r) // 2
            mergeSort(arr, l, m) # left side
            mergeSort(arr, m+1, r) # right side
            merge(arr, l, m, r) # merge everything back together
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
