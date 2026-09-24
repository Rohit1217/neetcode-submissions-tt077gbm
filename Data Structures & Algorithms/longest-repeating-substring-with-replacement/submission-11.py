
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq_hash=defaultdict(int)
        n=len(s)

        max_len=min(n,k)

        i=0
        j=max(0,k-1)
        max_freq=0

        for t in range(i,j):
            freq_hash[s[t]]+=1
            max_freq=max(max_freq,freq_hash[s[t]])
        
        while j<n:
            freq_hash[s[j]]+=1
            max_freq=max(max_freq,freq_hash[s[j]])

            if j-i+1-max_freq<=k:
                max_len=max(max_len,j-i+1)

            else:
                freq_hash[s[i]]-=1
                i+=1

            j+=1

        return max_len
