from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        # Let's do it with a min-heap. I'll just keep on inserting the elements by their (frequency, num) in the min heap. If the size of the heap grows beyond size k, then I'll just end up removing the minimum element from the heap. This will ensure that there are top k elements in the heap.
        # First, we'll need to build out the hashmap with nums and frequencies and then from that hashmap we can build a list of tuples that has the tuple shape (frequency, num), then we'll heapify that list and if the list size is more than k, we'll need to remove at most len - k stuff from the heap and then finally we can return the nums from our tuple
        # hashmap structure = {num : freq}
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        
        frequency_list = []
        for key, value in frequency_map.items():
            frequency_list.append((value, key))

        heapq.heapify(frequency_list)

        if len(frequency_list) > k:
            to_remove = len(frequency_list) - k
            for i in range(to_remove):
                heapq.heappop(frequency_list)

        # Now we just return the frequency count
        output = []

        for frequency, num in frequency_list:
            output.append(num)

        return output            