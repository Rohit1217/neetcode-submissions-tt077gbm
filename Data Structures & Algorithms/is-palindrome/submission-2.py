class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        allowed_charset=set("abcdefghijklmnopqrstuvwxyz0123456789")
        i=0
        j=len(s)-1
        while (i<j):
            if s[i] not in allowed_charset:
                i+=1
            elif s[j] not in allowed_charset:
                j-=1
            else:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
        return True