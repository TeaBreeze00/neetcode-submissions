from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        # Let's do the optimized plan: I'll run a loop stores the index as the
        # frequency and the content inside the index will be the list of the number itself
        # first we will store a hash map with keys will be nums and values will be frequency
        
        mymap = defaultdict(int)

        for num in nums:
            if(defaultdict[num]):
                mymap[num] += 1

        frequency = [[] for i in range(len(nums) + 1)]

        for nums in mymap:
            frequency[mymap[nums]].append(nums)
        
        res = []

        for i in range(len(frequency)-1, -1, -1):
            arr = frequency[i]

            for j in range(len(arr)):
                if len(res) >= k:
                    break
                res.append(arr[j])

        return res            


        
            



       
