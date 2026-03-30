class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1

        self.count=0
        
        def expand(l,r):
            while l>-1 and r<len(s) and s[l]==s[r]:
                self.count+=1
                l=l-1
                r=r+1
        
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)

        return self.count
    