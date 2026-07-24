class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # use mergesort to sort array
        # first part is splitting array into smaller halves recursively
        # need pointers for left and right sides of half
        # then merge back together by comparing vals
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            # adding to left pointer in main array and going from beginning
            # of each array being merged
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            # add in leftovers from whatever array isn't done
            while j < len(left):
                arr[i] = left[j]
                i += 1
                j += 1
            
            while k < len(right):
                arr[i] = right[k]
                i += 1
                k += 1

        def mergeSort(arr, l, r):
            # base case - arr size 1
            # check if pointers are equal
            if l == r:
                return arr
            # do same with left and right halves
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
