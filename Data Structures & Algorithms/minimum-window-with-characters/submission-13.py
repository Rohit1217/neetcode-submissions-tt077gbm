from collections import defaultdict,Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq_hash_t=Counter(t)
        freq_hash_s=defaultdict(int)
        
        num_matches=0

        i=0
        j=0

        min_window=len(s)+1
        min_i,min_j=0,0

        while j<len(s):
            freq_hash_s[s[j]]+=1

            if freq_hash_s[s[j]]==freq_hash_t[s[j]]:
                num_matches+=1
            
            while num_matches==len(freq_hash_t):
                if j-i+1<min_window:
                    min_i,min_j=i,j
                    min_window=j-i+1

                if freq_hash_s[s[i]]==freq_hash_t[s[i]]:
                    num_matches-=1
                
                freq_hash_s[s[i]]-=1
                i+=1
            
            j+=1

        if min_window==len(s)+1:
            return ""
        
        return s[min_i:min_j+1]
