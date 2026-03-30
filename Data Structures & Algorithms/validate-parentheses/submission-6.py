class Solution:
    def isValid(self, s: str) -> bool:
        length=len(s)
        left_brack=['(','{','[']
        d={'{':'}','(':')','[':']'}
        orientation="left"
        stack=[]
        count=0

        for i in range(len(s)):
            if s[i] in left_brack:
                stack.append(s[i])
                count+=1
            elif stack==[]:
                return False
            else:
                char=stack.pop()
                if s[i]!=d[char]:
                    return False
                else:
                    count-=1
        if count==0:
            return True
        return False
        