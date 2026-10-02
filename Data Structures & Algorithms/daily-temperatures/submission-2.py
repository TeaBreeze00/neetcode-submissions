class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Let's apply the monotonic stack approach to this problem. We will maintain a stack that has strictly decreasing order. So that if we get a temp that is more than the top of the stack, then we keep on popping the stack safely till we maintain a strictly decreasing order.
        Why does this approach work? Think of the stack as a snapshot of the array and the eleemnts that are strictly waiting for a warmer day to show up. So that we only track the elements that has not found a warmer day still and waiting for a warmer day to show up. After the iteration is over, if there are remaining element in the stack we just put 0 for them because we could not find warmer day for them.
        '''
        result = [0] * len(temperatures)
        min_stack = []

        for i in range(len(temperatures)):
            if not min_stack or temperatures[i] <= temperatures[min_stack[-1]]:
                min_stack.append(i)
            else:
                j = min_stack[-1]
                while min_stack and temperatures[i] > temperatures[min_stack[-1]]:
                    j = min_stack.pop()
                    result[j] = i - j
                min_stack.append(i)

        return result        

            
