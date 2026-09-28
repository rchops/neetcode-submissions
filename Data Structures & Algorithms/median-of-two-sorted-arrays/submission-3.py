class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # split full array into two partitions
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        # binary search on first array
        # then use idx for second array
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            # correct for 0 idx on both arrays
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # if partitioned correctly
            if Aleft <= Bright and Bleft <= Aright:
                # if even
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            # too many in left
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
