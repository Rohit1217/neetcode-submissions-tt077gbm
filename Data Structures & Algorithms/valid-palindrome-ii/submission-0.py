class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)    
    
        def is_palindrome(start,end):
            while start<end:
                if s[start]!=s[end]:
                    return 1,start,end
                else:
                    start+=1
                    end-=1
            return 0,start,end

        violations,start,end=is_palindrome(0,n-1)
        
        if violations>0:
           violations+=min(is_palindrome(start+1,end)[0],is_palindrome(start,end-1)[0]) 

        if violations>1:
            return False
        
        return True


        