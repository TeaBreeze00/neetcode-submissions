class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # we can do a simple search to find the index of the pivot element which takes
        # O(log n) time, if the target > nums[r], then it is to the left rotated portion,
        # if target <= nums[r], it is within the right portion of the array.
        # If the array is fully sorted, we just do vanilla binary search, otherwise we find pivot,
        # figure out which subportion the target lies and then we do vanilla binary search

        def binarySearch(l: int, r: int, target: int, nums: List[int]) -> int:

            while(l <= r):
                m = (l + r) // 2
                if(nums[m] == target):
                    return m
                elif target > nums[m]:
                    l = m + 1
                elif target <= nums[m]:
                    r = m - 1

            return -1    

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return binarySearch(l, r, target, nums)
    
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m    
        
        pivot = l

        if target > nums[-1]:
            return binarySearch(0, pivot - 1, target, nums)

        return binarySearch(pivot, len(nums) - 1, target, nums)   






