# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # If we merge it one-by-one, it'll be O(n.k^2) time complexity. Why? Because we need to merge first 2 list with O(n), then the size becomes 2n, so we merge 2n and n which takes 2n time, so it's n + 2n + 3n ... + (k-1)n which gives us: O(n*k^2) time complexity. 
        # A better way to do this would be to do it in pairs, which will give us log(k) levels of work, with doing upto n.k work at each level, bringing the total time complexity to n.k.log(k) or n*log(k) which is much more efficient. So pairwise merging is the best way to go.  
        if not lists:
            return None

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            curr = ListNode()
            head = curr
        
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next        
                curr = curr.next

            # After the operation, just attach the rest of the list whichever is not null
            curr.next = list1 or list2
            return head.next
        
        while len(lists) > 1:
            merged = [] # pairwise merging result
            n = len(lists)
            for i in range(0, n, 2):
                list_1 = lists[i]
                list_2 = lists[i+1] if i + 1 < n else None
                merged.append(mergeTwoLists(list_1, list_2))
            lists =  merged

        return lists[0]       


            