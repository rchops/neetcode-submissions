class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search to find best row
        # then binary search along that row
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows - 1
        best_row = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] == target:
                best_row = mid
                break
            elif matrix[mid][-1] > target:
                best_row = mid
                r = mid - 1
            else:
                l = mid + 1

        l_r, r_r = 0, cols - 1
        while l_r <= r_r:
            mid = (l_r + r_r) // 2
            if matrix[best_row][mid] == target:
                return True
            elif matrix[best_row][mid] > target:
                r_r = mid - 1
            else:
                l_r = mid + 1

        return False