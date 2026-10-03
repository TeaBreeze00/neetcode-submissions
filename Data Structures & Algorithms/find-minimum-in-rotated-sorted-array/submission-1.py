class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        # This is the idea, I will first find the median of the leftmost and 
        # rightmost endpoint, if the median is greater than the rightmost value,
        # we can conclude that the median now lies in the left rotated portion of the array
        # and we have to search 1 position to the right of the median to shrink our search space
        # if the median is not greater than the rightmost element, then it means the array is sorted 
        # properly and we just search to the left of the array to get closer and closer to our requested
        # value, after the binary search runs, we just return the leftmost value of the array. arr[l]

        while l < r:
            m = (l + r) // 2
            # we only change m if it's to the left rotated part, otherwise it stays the same?
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]            
