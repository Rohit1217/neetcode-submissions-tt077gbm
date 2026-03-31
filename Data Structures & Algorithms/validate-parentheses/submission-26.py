from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        val_map=defaultdict(str)
        val_map["("]=")"
        val_map["["]="]"
        val_map["{"]="}"

        stack=[]
        for char in s:
            stack.append(char)
            if len(stack)>1 and stack[-1]==val_map[stack[-2]]:       
                stack.pop(),stack.pop()

            print(stack,"V")
        if len(stack)>0:
            return False

        return True