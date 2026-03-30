from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        n=len(s)
        
        start=0
        end=0
        char_count=defaultdict(int)
        global_max=0
        ans=0
        
        while end!=n:
            char_count[s[end]]+=1
            global_max=max(global_max,char_count[s[end]])

            if global_max<(end-start+1-k):
                char_count[s[start]]-=1
                start+=1
                
            ans=max(ans,end-start+1)
            end+=1
        

        return ans

