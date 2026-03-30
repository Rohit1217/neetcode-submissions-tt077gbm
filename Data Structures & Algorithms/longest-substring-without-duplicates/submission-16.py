from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)

        if n<2:
            return n

        pos_hash=defaultdict(lambda: -1)

        start,end=0,0
        res_len=0
        curr_len=0

        while end<n:
            if pos_hash[s[end]]>=start:
                start=pos_hash[s[end]]
                curr_len=end-start-1
            
            pos_hash[s[end]]=end
            end+=1
            curr_len+=1
            print(curr_len,start)
            res_len=max(res_len,curr_len)
        
        return res_len

