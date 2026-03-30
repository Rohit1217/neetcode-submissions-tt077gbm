class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        elif len(s)<k:
            return len(s)
        
        freq_count={}
        left_idx=0
        right_idx=0
        max_len=1
        most_freq=0

        while right_idx<len(s):            
            
            if s[right_idx] not in freq_count:
                freq_count[s[right_idx]]=1 
            else:
                freq_count[s[right_idx]]+=1
            
            most_freq=max(most_freq,freq_count[s[right_idx]])

            if right_idx-left_idx+1-most_freq>k:
                freq_count[s[left_idx]]-=1
                left_idx+=1

            max_len=max(max_len,right_idx-left_idx+1)
            right_idx+=1
        
        return max_len
