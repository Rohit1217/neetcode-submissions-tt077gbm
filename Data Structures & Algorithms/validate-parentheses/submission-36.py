class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        stack=[]
        n=len(s)

        for i in range(n):
            if s[i] in  "({[":
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                brkt=stack.pop()

                if brkt+s[i] not in ["()","{}","[]"]:
                    return False
        
        if stack==[]:
            return True
        
        return False
                    


