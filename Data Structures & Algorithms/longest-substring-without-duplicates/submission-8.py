class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s)==0:
            return 0

        last_pos_char={}
        left_idx=0
        last_pos_char[s[left_idx]]=0
        right_idx=1
        max_length=1

        while right_idx<=len(s)-1:
            curr_char=s[right_idx]
            if curr_char not in last_pos_char or last_pos_char[curr_char]<left_idx:
                max_length=max(max_length,right_idx-left_idx+1)
            else:
                left_idx=last_pos_char[curr_char]+1
            
            last_pos_char[curr_char]=right_idx
            right_idx+=1
        
        return max_length