class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)

        def len_max_pali(i):
            even_len=0
            if i+1<n:
                if s[i]==s[i+1]:
                    p1,p2=i,i+1
                    while p1>-1 and p2<n  and s[p1]==s[p2]:
                        even_len+=2
                        p1-=1
                        p2+=1
            odd_len=1
            p1,p2=i-1,i+1
            while p1>-1 and p2<n  and s[p1]==s[p2]:
                odd_len+=2
                p1-=1
                p2+=1
            
            return max(even_len,odd_len)
        
        max_len=0
        prev_len=0
        for i in range(0,n):
            max_len=max(max_len,len_max_pali(i))
        
            if max_len>prev_len:
                prev_len=max_len
                max_idx=i
    
        i=max_idx

        even_len=0
        even_pal=""
        if i+1<n:
            if s[i]==s[i+1]:
                p1,p2=i,i+1
                while p1>-1 and p2<n  and s[p1]==s[p2]:
                    even_len+=2
                    even_pal=s[p1]+even_pal+s[p2]
                    p1-=1
                    p2+=1
        odd_len=1
        odd_pal=s[i]
        p1,p2=i-1,i+1
        while p1>-1 and p2<n  and s[p1]==s[p2]:
            odd_len+=2
            odd_pal=s[p1]+odd_pal+s[p2]
            p1-=1
            p2+=1
        
        if odd_len==max_len:
            return odd_pal
        return even_pal