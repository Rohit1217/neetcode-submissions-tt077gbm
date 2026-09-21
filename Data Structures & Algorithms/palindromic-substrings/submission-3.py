class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)

        def len_max_pali(i):
            num_pal=1
            if i+1<n:
                if s[i]==s[i+1]:
                    p1,p2=i,i+1
                    while p1>-1 and p2<n  and s[p1]==s[p2]:
                        p1-=1
                        p2+=1
                        num_pal+=1
            p1,p2=i-1,i+1
            while p1>-1 and p2<n  and s[p1]==s[p2]:
                p1-=1
                p2+=1
                num_pal+=1
            
            return num_pal

        count_pal=0

        for i in range(0,n):
            count_pal+=len_max_pali(i)        
        
        return count_pal