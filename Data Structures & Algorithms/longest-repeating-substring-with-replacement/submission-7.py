from collections import defaultdict        
class Solution:
    def characterReplacement(self,s,k):
        if s=="":
            return 0
        
        left=0
        right=0
        curr_max_val=1
        max_wind_size=1
        char_count=defaultdict(int)
        
        # char_count[s[0]]+=1

        while right<len(s):
            char_count[s[right]]+=1
            curr_max_val=max(curr_max_val,char_count[s[right]])

            if (right-left+1-curr_max_val)>k: 
                print(left,right,curr_max_val)   
                char_count[s[left]]-=1
                left=left+1
            else:
                max_wind_size=max(max_wind_size,right-left+1)
            
            right+=1

        return  max_wind_size  

