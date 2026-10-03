class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            m = (top + bottom) // 2

            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                break
        else:
            return False   # loop ended without finding a candidate row

        # here, m is the row whose range contains target
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[m][mid]:
                l = mid + 1
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                return True

        return False