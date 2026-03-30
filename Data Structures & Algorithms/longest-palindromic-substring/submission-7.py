class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        elif len(s)==1:
            return s[0]
        self.idx=0,0
        self.maxm=1
        
        def expand(l,r):
            while l>-1 and r<len(s) and s[l]==s[r]:
                if r-l+1>self.maxm:
                    self.maxm=r-l+1
                    self.idx=l,r
                l=l-1
                r=r+1
        
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        i,j=self.idx
        return s[i:j+1]
    