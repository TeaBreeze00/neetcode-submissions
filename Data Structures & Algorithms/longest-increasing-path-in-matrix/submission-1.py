class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Let's think about this in a cell traversal perspective, in any cell, I can decide on if I need to move top, left, right or bottom, if it's strictly greater than my current value, then I only choose the maximum out of the 4 paths
        # So dp[i][j] will indicate the longest increasing path that we can make starting with the index i, j
        # So, dp[i][j] = max (each of up, down, left, right dp if they are not out of bounds)
        # So, what is the bottom-up dp approach here? For bottom up, the order of the processing matters in this case. We have to start from processing the biggest element in the array first before we move on to smaller cells, because we ask the question in that order. So, we make another matrix where we rearrange by descending order and then process it in that order.

        m = len(matrix)
        n = len(matrix[0])
        dp = [[1] * n for _ in range(m)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        flat = []
        for i in range(m):
            for j in range(n):
                tuple_item = (matrix[i][j], i, j)
                flat.append(tuple_item)

        flat.sort(reverse=True) # Flatten the matrix and then sort them by their value

        for val, i, j in flat:
            for dir_x, dir_y in dirs:
                updated_x = i + dir_x
                updated_y = j + dir_y
                if (0 <= updated_x < m and 0 <= updated_y < n):
                    if(matrix[updated_x][updated_y] > matrix[i][j]):
                        dp[i][j] = max(dp[i][j], 1 + dp[updated_x][updated_y])
        
        # Just find the max and return
        maximum = -1
        for i in range(m):
            for j in range(n):
                if dp[i][j] >= maximum:
                    maximum = dp[i][j]

        return maximum            