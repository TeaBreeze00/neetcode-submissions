class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "}":"{", "]":"["}
        stack = []

        for bracket in s:
            if bracket in brackets.values(): # If it's an opening bracket, add it
                stack.append(bracket)
            else:
                if len(stack) > 0:
                    top = stack[-1]
                    if top == brackets[bracket]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False        


        return True if not stack else False          
