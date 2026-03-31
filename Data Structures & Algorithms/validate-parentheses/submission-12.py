class Solution:
    def isValid(self, s: str) -> bool:
        
        def reverse(s):
            if s=="(":
                return ")"
            elif s=="{":
                return "}"
            else:
                return "]"
        
        left_brackets=["{","[","("]

        stack=[]
        for char in s:
            if char in left_brackets:
                stack.append(char)
            elif len(stack)==0:
                return False
            else:
                curr_val=stack.pop()
                if reverse(curr_val)!=char:
                    return False
        
        if len(stack)>0:
            return False

        return True