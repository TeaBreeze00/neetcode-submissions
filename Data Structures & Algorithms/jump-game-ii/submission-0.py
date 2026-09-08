class Solution:
    def jump(self, nums: List[int]) -> int:
        # Let's solve this using greedy approach now. The key idea is to prevent blowing of the recursive tree, we should maintain a range and carry forward the range. This video has a good explanation: https://www.youtube.com/watch?v=7SBVnw7GSTk. The jump number at the end of the iteration will be the answer
        left = 0
        right = 0
        jump = 0

        while right < len(nums) - 1:
            max_jump = 0
            for i in range(left, right + 1):
                max_jump = max(max_jump, nums[i] + i)   
            left = right + 1
            right = max_jump 
            jump += 1

        return jump    