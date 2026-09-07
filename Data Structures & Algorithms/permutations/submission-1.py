class Solution:
    # Here for each time, I'll have choice upto the elements that I currently have on the list: after I make a specific choice, I can remove that element from my choice of elements and continue, when we hit that we have no elements in the list, we can append the entire subarray to our answer list. We can do something like taking the diff of nums and curr and go from there. So, every step we have to iterate through the difference of curr and the main nums list, then select each of them one by one and we return when we see that difference is 0, i.e we explored all elements in the array

    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

        def backtrack(curr: List[int]):
            diff = list(set(nums) - set(curr))

            if len(diff) == 0:
                res.append(curr[:]) 
                return

            for elem in diff:
                curr.append(elem)
                backtrack(curr)
                curr.pop()         

        backtrack(curr)
        return res                     
        